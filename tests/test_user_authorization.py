class TestUserAuthorization:

    def test_successful_user_authorization_returns_201(self, authorized_user_response):
        assert authorized_user_response.status_code == 201

    def test_successful_user_authorization_contains_user_field(self, authorized_user_response):
        response_data = authorized_user_response.json()
        assert 'user' in response_data

    def test_successful_user_authorization_contains_token_field(self, authorized_user_response):
        response_data = authorized_user_response.json()
        assert 'token' in response_data

    def test_successful_user_authorization_returns_correct_email(self, authorized_user_response):
        response_data = authorized_user_response.json()
        assert response_data['user']['email'] == authorized_user_response.user_data['email']
