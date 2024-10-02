import pytest
from src.YahooFantasyAPI.api_client import APIClient


def test_only_url_request():
    client = APIClient()
    res = client.get('https://www.google.ca')
    assert res.status_code == 200