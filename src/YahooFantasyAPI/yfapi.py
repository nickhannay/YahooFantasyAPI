from .auth import TokenManager
from .api_client import APIClient
from .collections import team
import json

BASE_URL = "https://fantasysports.yahooapis.com/fantasy/v2"


class YFAPI:
    '''
    A class that can be used to easily interface with the Yahoo Fantasy Sports API

    Attributes:
        client_id (str): Client id assigned to the app by Yahoo
        client_secret (str): Client secret assigned to the app by Yahoo
        redirect_uri (str, optional): The uri Yahoo will redirect to upon authorization. Defaults to 'oob' (out of band)
    Methods:
        generate_auth_url(): Creates the url used to prompt the user for authorization
        generate_token(auth_code): Generates a token from the yahoo generated authorization code
    '''
    def __init__(self, client_id, client_secret, redirect_uri='oob'):
        self.token_manager = TokenManager(client_id, client_secret, redirect_uri)
        self.api_client = APIClient(base_url=BASE_URL)

    def get_auth_url(self):
        return self.token_manager.auth_url

    def generate_token(self, user_id, auth_code):
        token = self.token_manager.generate_user_token(user_id, auth_code)
        return token

    def get_teams(self, user_id, team_ids=None):
        token = self.token_manager.get_valid_user_token(user_id)
        teams = team.get_teams(token=token, client=self.api_client, team_keys=team_ids)
        return teams

    def get_roster(self, user_id, team_key):
        token = self.token_manager.get_valid_user_token(user_id)
        roster = team.get_roster(token, self.api_client, team_key)
        return roster
    
    def get_stats(self, user_id, team_key):
        token = self.token_manager.get_valid_user_token(user_id)
        stats = team.get_stats(token, self.api_client, team_key)
        return stats