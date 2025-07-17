import pytest
import requests
from data.config import Config
from data.endpoints import APIEndpoints
from data.test_data import TestConstants
from helpers import EmailGenerator, APIHelpers


class APIClient:
    """Клиент для работы с API"""
    
    def __init__(self, base_url=Config.BASE_URL, timeout=Config.API_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def post(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.post(url, **kwargs)
    
    def get(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.get(url, **kwargs)
    
    def patch(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.patch(url, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.delete(url, **kwargs)
    
    def post_multipart(self, endpoint, data=None, files=None, headers=None, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        
        request_headers = self.session.headers.copy()
        if headers:
            request_headers.update(headers)
        
        return self.session.post(url, data=data, files=files, headers=request_headers, **kwargs)


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def fake_image():
    return b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xdd\x8d\xb4\x1c\x00\x00\x00\x00IEND\xaeB`\x82'


@pytest.fixture
def registered_user_response(api_client):
    user_data = {
        'email': EmailGenerator.generate_unique_email(),
        'password': TestConstants.DEFAULT_PASSWORD
    }
    
    response = api_client.post(APIEndpoints.REGISTER, json=user_data)
    response.user_data = user_data
    return response


@pytest.fixture
def duplicate_registration_response(api_client):
    user_data = {
        'email': EmailGenerator.generate_unique_email(),
        'password': TestConstants.DEFAULT_PASSWORD
    }
    
    first_response = api_client.post(APIEndpoints.REGISTER, json=user_data)
    assert first_response.status_code == 201
    
    second_response = api_client.post(APIEndpoints.REGISTER, json=user_data)
    return second_response


@pytest.fixture
def authorized_user_response(api_client, registered_user_response):
    assert registered_user_response.status_code == 201
    
    response = api_client.post(APIEndpoints.LOGIN, json=registered_user_response.user_data)
    response.user_data = registered_user_response.user_data
    return response


@pytest.fixture
def created_ad_response(api_client, authorized_user_response, fake_image):
    assert authorized_user_response.status_code == 201
    token = authorized_user_response.json()['token']['access_token']
    
    files = {
        'images': ('test.png', fake_image, 'image/png')
    }
    
    response = api_client.post_multipart(
        APIEndpoints.CREATE_AD, 
        data=TestConstants.DEFAULT_AD_DATA,
        files=files,
        headers={'Authorization': f'Bearer {token}'}
    )
    response.token = token
    return response


@pytest.fixture
def edited_ad_response(api_client, created_ad_response):
    assert created_ad_response.status_code == 201
    created_ad = created_ad_response.json()
    
    updates = {'name': TestConstants.EDITED_AD_NAME}
    update_data = APIHelpers.prepare_ad_update_data(created_ad, updates)
    
    api_client.session.headers.update({'Authorization': f'Bearer {created_ad_response.token}'})
    response = api_client.patch(f"{APIEndpoints.UPDATE_AD}/{created_ad['id']}", json=update_data)
    response.updated_name = TestConstants.EDITED_AD_NAME
    return response


@pytest.fixture
def other_user_edit_attempt_response(api_client, created_ad_response):
    assert created_ad_response.status_code == 201
    created_ad = created_ad_response.json()
    
    user2_data = {
        'email': EmailGenerator.generate_unique_email(),
        'password': TestConstants.DEFAULT_PASSWORD
    }
    
    register_response2 = api_client.post(APIEndpoints.REGISTER, json=user2_data)
    assert register_response2.status_code == 201
    
    login_response2 = api_client.post(APIEndpoints.LOGIN, json=user2_data)
    assert login_response2.status_code == 201
    token2 = login_response2.json()['token']['access_token']
    
    updates = {'name': TestConstants.OTHER_USER_AD_EDIT_ATTEMPT_NAME}
    update_data = APIHelpers.prepare_ad_update_data(created_ad, updates)
    
    api_client.session.headers.update({'Authorization': f'Bearer {token2}'})
    response = api_client.patch(f"{APIEndpoints.UPDATE_AD}/{created_ad['id']}", json=update_data)
    return response


@pytest.fixture
def deleted_ad_response(api_client, created_ad_response):
    assert created_ad_response.status_code == 201
    created_ad = created_ad_response.json()
    
    api_client.session.headers.update({'Authorization': f'Bearer {created_ad_response.token}'})
    response = api_client.delete(f"{APIEndpoints.DELETE_AD}/{created_ad['id']}")
    return response
