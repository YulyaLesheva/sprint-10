from data.endpoints import APIEndpoints
from data.test_data import TestConstants
from helpers import EmailGenerator, APIHelpers


class TestAdEditing:

    def test_successful_ad_editing_returns_200(self, api_client, authorized_user, fake_image):
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
        
        updates = {'name': TestConstants.EDITED_AD_NAME}
        update_data = APIHelpers.prepare_ad_update_data(created_ad, updates)
        
        edit_response = api_client.patch(
            f"{APIEndpoints.UPDATE_AD}/{created_ad['id']}", 
            json=update_data,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        assert edit_response.status_code == 200

    def test_successful_ad_editing_returns_updated_name(self, api_client, authorized_user, fake_image):
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
        
        updates = {'name': TestConstants.EDITED_AD_NAME}
        update_data = APIHelpers.prepare_ad_update_data(created_ad, updates)
        
        edit_response = api_client.patch(
            f"{APIEndpoints.UPDATE_AD}/{created_ad['id']}", 
            json=update_data,
            headers={'Authorization': f'Bearer {authorized_user["token"]}'}
        )
        response_data = edit_response.json()
        assert response_data['name'] == TestConstants.EDITED_AD_NAME

    def test_edit_other_user_ad_returns_401_status(self, api_client, authorized_user, fake_image):
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
        
        user2_data = {
            'email': EmailGenerator.generate_unique_email(),
            'password': TestConstants.DEFAULT_PASSWORD
        }
        api_client.post(APIEndpoints.REGISTER, json=user2_data)
        
        login_response2 = api_client.post(APIEndpoints.LOGIN, json=user2_data)
        token2 = login_response2.json()['token']['access_token']
        
        updates = {'name': TestConstants.OTHER_USER_AD_EDIT_ATTEMPT_NAME}
        update_data = APIHelpers.prepare_ad_update_data(created_ad, updates)
        
        edit_response = api_client.patch(
            f"{APIEndpoints.UPDATE_AD}/{created_ad['id']}", 
            json=update_data,
            headers={'Authorization': f'Bearer {token2}'}
        )
        assert edit_response.status_code == 401
