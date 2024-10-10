import pytest
import webbrowser
import json
import os
from dotenv import load_dotenv
from src.yfsAPI import YFAPI

load_dotenv('../.env')

@pytest.fixture
def yfsAPI():
    return YFAPI(os.environ.get('client_id'), os.environ.get('client_secret'))

def test_get_user_teams(yfsAPI):
    url = yfsAPI.get_auth_url()
    webbrowser.open(url)
    code = input('input auth code: ')
    yfsAPI.generate_token('id1', code)
    teams = yfsAPI.get_teams('id1')
    print(json.dumps(teams, indent=4))

