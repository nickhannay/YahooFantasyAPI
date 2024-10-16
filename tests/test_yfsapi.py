import pytest
import webbrowser
import time
import os
from dotenv import load_dotenv
from src.yfsAPI import yfsAPI, yfsInvalidRedirectURIException, yfsInvalidAuthCodeException
from src.yfsAPI.auth import Token

load_dotenv('../.env')

@pytest.fixture
def get_yfsAPI():
    def _create_yfs_api(uri='oob') -> yfsAPI:
        return yfsAPI(os.environ.get('client_id'), os.environ.get('client_secret'), uri)
    return _create_yfs_api

def test_yfs_valid_auth_code(get_yfsAPI):
    yfs_api = get_yfsAPI()
    url = yfs_api.get_auth_url()
    print(url)
    webbrowser.open(url)
    code = input('input auth code: ')
    res = yfs_api.generate_token('id1', code)
    print(res['token'])
    token = res['token']
    assert isinstance(token, Token)
    assert hasattr(token, 'access_token')
    assert hasattr(token, 'refresh_token')
    assert token.created_at <= time.time()


def test_yfs_invalid_auth_code(get_yfsAPI):
    with pytest.raises(yfsInvalidAuthCodeException):
        yfs_api = get_yfsAPI()
        yfs_api.generate_token('id2', 'sdffsd')


def test_yfs_invalid_redirect(get_yfsAPI):
    with pytest.raises(yfsInvalidRedirectURIException):
        api = get_yfsAPI('httc://fake.ca')
        webbrowser.open(api.get_auth_url())
        code = input('auth code: ') 
        api.generate_token('id5', code)