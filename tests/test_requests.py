import pytest
from src.YahooFantasyAPI.request import make_request

def test_only_url_request():
    res = make_request('https://www.google.ca')
    assert res.status_code == 200