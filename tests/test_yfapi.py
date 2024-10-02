import pytest
import webbrowser
import json
from src.YahooFantasyAPI import YFAPI


client_id = 'dj0yJmk9cUZJNmFsUTY0WFc1JmQ9WVdrOWVURTVTVEpWTmtzbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTcx'
client_secret = '6013d66a85f94f7c938f1fa042b60e16a44e9d87'
redirect_uri = 'https://localhost:4500/auth/callback'

def test_get_user_teams():
    yf_api = YFAPI(client_id, client_secret, redirect_uri)
    url = yf_api.get_auth_url()
    webbrowser.open(url)
    code = input('input auth code: ')
    yf_api.generate_token('id1', code)
    teams = yf_api.get_teams('id1')
    print(json.dumps(teams, indent=4))

