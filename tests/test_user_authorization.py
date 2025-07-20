from data.endpoints import APIEndpoints
from data.test_data import TestConstants
from helpers import EmailGenerator


class TestUserAuthorization:

    def test_successful_user_authorization_returns_201(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        api_client.post(APIEndpoints.REGISTER, json=user_data)
        
        login_response = api_client.post(APIEndpoints.LOGIN, json=user_data)
        assert login_response.status_code == 201

    def test_successful_user_authorization_contains_user_field(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        api_client.post(APIEndpoints.REGISTER, json=user_data)
        
        login_response = api_client.post(APIEndpoints.LOGIN, json=user_data)
        response_data = login_response.json()
        assert 'user' in response_data

    def test_successful_user_authorization_contains_token_field(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        api_client.post(APIEndpoints.REGISTER, json=user_data)
        
        login_response = api_client.post(APIEndpoints.LOGIN, json=user_data)
        response_data = login_response.json()
        assert 'token' in response_data

    def test_successful_user_authorization_returns_correct_email(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        api_client.post(APIEndpoints.REGISTER, json=user_data)
        
        login_response = api_client.post(APIEndpoints.LOGIN, json=user_data)
        response_data = login_response.json()
        assert response_data['user']['email'] == user_data['email']
