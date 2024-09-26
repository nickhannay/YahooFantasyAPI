import pytest
import webbrowser

from src.YahooFantasyAPI.auth import generate_url, generate_hash, generate_token

client_id = 'dj0yJmk9cUZJNmFsUTY0WFc1JmQ9WVdrOWVURTVTVEpWTmtAdkiRH934DGsdf9JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTcx'
client_secret = '6013d66a8sdfs34UsiI38f1fa042b60e16a44e9d87'
redirect_uri = 'https://test.ca'

def test_auth_url():
    url = generate_url(client_id, redirect_uri)
    assert url == f'https://api.login.yahoo.com/oauth2/request_auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&language=en-us'


def test_auth_url_noredirect():
    url = generate_url(client_id)
    assert url == f'https://api.login.yahoo.com/oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'


'''
def test_generate_token():
    auth_url = generate_auth_url(client_id)
    webbrowser.open(auth_url)
    auth_code = input('enter auth code: ')
    auth_hash = generate_hash(client_id, client_secret)
    token = generate_token(auth_code, auth_hash)
    print(token)
'''

def test_generate_hash():
    hash_r = generate_hash(client_id, client_secret)
    assert hash_r == 'ZGoweUptazljVVpKTm1Gc1VUWTBXRmMxSm1ROVdWZHJPV1ZVUlRWVFZFcFdUbXRBZGtpUkg5MzRER3NkZjlKbk05WTI5dWMzVnRaWEp6WldOeVpYUW1jM1k5TUNaNFBUY3g6NjAxM2Q2NmE4c2RmczM0VXNpSTM4ZjFmYTA0MmI2MGUxNmE0NGU5ZDg3'