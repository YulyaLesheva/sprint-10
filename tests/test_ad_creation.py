from data.endpoints import APIEndpoints
from data.test_data import TestConstants


class TestAdCreation:

    def test_successful_ad_creation_returns_201(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        
        response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        assert response.status_code == 201

    def test_successful_ad_creation_contains_id_field(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        
        response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        response_data = response.json()
        assert 'id' in response_data

    def test_successful_ad_creation_returns_correct_name(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        
        response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        response_data = response.json()
        assert response_data['name'] == TestConstants.DEFAULT_AD_DATA['name']

    def test_successful_ad_creation_returns_correct_category(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        
        response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        response_data = response.json()
        assert response_data['category'] == TestConstants.DEFAULT_AD_DATA['category']
