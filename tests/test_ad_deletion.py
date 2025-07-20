from data.endpoints import APIEndpoints
from data.test_data import TestConstants


class TestAdDeletion:

    def test_successful_ad_deletion_returns_200(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        create_response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        created_ad = create_response.json()
        
        delete_response = api_client.delete(
            f"{APIEndpoints.DELETE_AD}/{created_ad['id']}",
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        assert delete_response.status_code == 200

    def test_successful_ad_deletion_returns_success_message(self, api_client, authorized_user, fake_image):
        files = {
            'images': ('test.png', fake_image, 'image/png')
        }
        create_response = api_client.post_multipart(
            APIEndpoints.CREATE_AD, 
            data=TestConstants.DEFAULT_AD_DATA,
            files=files,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        created_ad = create_response.json()
        
        delete_response = api_client.delete(
            f"{APIEndpoints.DELETE_AD}/{created_ad['id']}",
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        response_data = delete_response.json()
        assert response_data['message'] == TestConstants.AD_DELETION_SUCCESS_MESSAGE
