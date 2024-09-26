from .auth import auth
import httpx 


class YFAPI:
    '''
    A class that can be used to easily interface with the Yahoo Fantasy Sports API

    Attributes:
        client_id (str): Client id assigned to the app by Yahoo
        client_secret (str): Client secret assigned to the app by Yahoo
        redirect_uri (str, optional): The uri yahoo will redirect to upon authorization. Defaults to 'oob'  
    Methods:
        generate_auth_url(): Creates the url used to prompt the user for authorization
        generate_token(auth_code): Generates a token from the provided authorization code
    '''
    def __init__(self, client_id, client_secret, redirect_uri='oob'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.http_client = httpx.Client()

    def generate_auth_url(self):
        return auth.generate_url(self.client_id, self.redirect_uri)

    def generate_token(self, auth_code):
        auth_hash = auth.generate_hash(self.client_id, self.client_secret)
        token = auth.generate_token(auth_code, auth_hash, self.redirect_uri)
        self.http_client.headers = {'Authorization': f'Bearer {token.access_token}'}
        return token

    '''def get_leagues(league_ids=None):
        

    def get_teams():'''




