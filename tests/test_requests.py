import pytest
from src.yfsAPI.api_client import APIClient, APIClientException


@pytest.fixture
def api_client():
    return APIClient()


def test_get_invalid_url(api_client):
    with pytest.raises(APIClientException):
        api_client.get('httwerw://www.google.ca')


def test_post_invalid_url(api_client):
    with pytest.raises(APIClientException):
        api_client.post('httwerw://www.google.ca')


def test_get_url(api_client):
    res = api_client.get('https://www.google.ca')
    assert res.status_code == 200

