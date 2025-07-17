from data.test_data import TestConstants


class TestAdDeletion:

    def test_successful_ad_deletion_returns_200(self, deleted_ad_response):
        assert deleted_ad_response.status_code == 200

    def test_successful_ad_deletion_returns_success_message(self, deleted_ad_response):
        response_data = deleted_ad_response.json()
        assert response_data['message'] == TestConstants.AD_DELETION_SUCCESS_MESSAGE
