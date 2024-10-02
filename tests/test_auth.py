import pytest
import webbrowser

from src.YahooFantasyAPI.auth import TokenManager
from src.YahooFantasyAPI.auth.token_manager import generate_hash

client_id = 'dj0yJmk9cUZJNmFsUTY0WFc1JmQ9WVdrOWVURTVTVEpWTmtzbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTcx'
client_secret = '6013d66a85f94f7c938f1fa042b60e16a44e9d87'
redirect_uri = 'https://localhost:4500/auth/callback'


def test_auth_url():
    token_manager = TokenManager(client_id, client_secret, redirect_uri)
    url = token_manager.auth_url
    assert url == f'https://api.login.yahoo.com/oauth2/request_auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&language=en-us'


def test_generate_token():
    tm = TokenManager(client_id, client_secret, redirect_uri)
    webbrowser.open(tm.auth_url)
    auth_code = input('enter auth code: ')
    token = tm.generate_user_token('faef48y4ggb', auth_code)
    print(token)


def test_generate_hash():
    hash_r = generate_hash(client_id, client_secret)
    assert hash_r == 'ZGoweUptazljVVpKTm1Gc1VUWTBXRmMxSm1ROVdWZHJPV1ZVUlRWVFZFcFdUbXRBZGtpUkg5MzRER3NkZjlKbk05WTI5dWMzVnRaWEp6WldOeVpYUW1jM1k5TUNaNFBUY3g6NjAxM2Q2NmE4c2RmczM0VXNpSTM4ZjFmYTA0MmI2MGUxNmE0NGU5ZDg3'