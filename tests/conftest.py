import pytest
from api_client import APIClient
from data.endpoints import APIEndpoints
from data.test_data import TestConstants
from helpers import EmailGenerator


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def fake_image():
    return b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xdd\x8d\xb4\x1c\x00\x00\x00\x00IEND\xaeB`\x82'


@pytest.fixture
def authorized_user(api_client):
    user_data = {
        'email': EmailGenerator.generate_unique_email(),
        'password': TestConstants.DEFAULT_PASSWORD
    }
    
    api_client.post(APIEndpoints.REGISTER, json=user_data)
    
    login_response = api_client.post(APIEndpoints.LOGIN, json=user_data)
    token = login_response.json()['token']['access_token']
    
    return {
        'user_data': user_data,
        'token': token
    }
