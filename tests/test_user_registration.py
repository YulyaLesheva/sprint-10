class TestUserRegistration:

    def test_successful_user_registration_returns_201(self, registered_user_response):
        assert registered_user_response.status_code == 201

    def test_successful_user_registration_contains_user_field(self, registered_user_response):
        response_data = registered_user_response.json()
        assert 'user' in response_data

    def test_successful_user_registration_contains_access_token(self, registered_user_response):
        response_data = registered_user_response.json()
        assert 'access_token' in response_data

    def test_successful_user_registration_returns_correct_email(self, registered_user_response):
        response_data = registered_user_response.json()
        assert response_data['user']['email'] == registered_user_response.user_data['email']

    def test_duplicate_email_registration_returns_400(self, duplicate_registration_response):
        assert duplicate_registration_response.status_code == 400
