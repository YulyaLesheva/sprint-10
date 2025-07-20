from data.endpoints import APIEndpoints
from data.test_data import TestConstants
from helpers import EmailGenerator


class TestUserRegistration:

    def test_successful_user_registration_returns_201(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        
        response = api_client.post(APIEndpoints.REGISTER, json=user_data)
        assert response.status_code == 201

    def test_successful_user_registration_contains_user_field(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        
        response = api_client.post(APIEndpoints.REGISTER, json=user_data)
        response_data = response.json()
        assert 'user' in response_data

    def test_successful_user_registration_contains_access_token(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        
        response = api_client.post(APIEndpoints.REGISTER, json=user_data)
        response_data = response.json()
        assert 'access_token' in response_data

    def test_successful_user_registration_returns_correct_email(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        
        response = api_client.post(APIEndpoints.REGISTER, json=user_data)
        response_data = response.json()
        assert response_data['user']['email'] == user_data['email']

    def test_duplicate_email_registration_returns_400(self, api_client):
        user_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        
        api_client.post(APIEndpoints.REGISTER, json=user_data)
        
        second_response = api_client.post(APIEndpoints.REGISTER, json=user_data)
        assert second_response.status_code == 400
