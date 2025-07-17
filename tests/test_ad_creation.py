from data.test_data import TestConstants


class TestAdCreation:

    def test_successful_ad_creation_returns_201(self, created_ad_response):
        assert created_ad_response.status_code == 201

    def test_successful_ad_creation_contains_id_field(self, created_ad_response):
        response_data = created_ad_response.json()
        assert 'id' in response_data

    def test_successful_ad_creation_returns_correct_name(self, created_ad_response):
        response_data = created_ad_response.json()
        assert response_data['name'] == TestConstants.DEFAULT_AD_DATA['name']

    def test_successful_ad_creation_returns_correct_category(self, created_ad_response):
        response_data = created_ad_response.json()
        assert response_data['category'] == TestConstants.DEFAULT_AD_DATA['category']
