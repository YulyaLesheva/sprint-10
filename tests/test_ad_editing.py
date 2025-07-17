

class TestAdEditing:

    def test_successful_ad_editing_returns_200(self, edited_ad_response):
        assert edited_ad_response.status_code == 200

    def test_successful_ad_editing_returns_updated_name(self, edited_ad_response):
        response_data = edited_ad_response.json()
        assert response_data['name'] == edited_ad_response.updated_name

    def test_edit_other_user_ad_returns_401_status(self, other_user_edit_attempt_response):
        assert other_user_edit_attempt_response.status_code == 401
