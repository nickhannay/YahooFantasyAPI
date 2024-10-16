from .token import Token
from ..api_client import APIClient, InvalidRequestException, FailedRequestException, APIClientException
import json
import base64

TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
AUTH_URL = "https://api.login.yahoo.com/oauth2/request_auth"


def generate_hash(client_id, client_secret):
    base_string_bytes = f'{client_id}:{client_secret}'.encode()
    hash_encoded = base64.b64encode(base_string_bytes)
    return hash_encoded.decode()


class TokenManager():
    def __init__(self, client_id, client_secret, redirect_uri="oob"):
        self.auth_url = f'{AUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&language=en-us'
        self.tokens = {}
        self.redirect_uri = redirect_uri
        self.auth_hash = generate_hash(client_id, client_secret)
        self.api_client = APIClient(base_headers={'Authorization': f'Basic {self.auth_hash}'})

    def generate_user_token(self, user_id, auth_code):
        try:
            res = self.api_client.post(url=TOKEN_URL,
                                    data={'grant_type': 'authorization_code',
                                            'redirect_uri': self.redirect_uri,
                                            'code': auth_code})
            res_json = json.loads(res.content)
            token = Token(res_json["access_token"], res_json["refresh_token"], res_json["expires_in"])
            self.tokens[user_id] = token
            return token
        
        except InvalidRequestException as e:
            match e.name:
                case 'INVALID_AUTHORIZATION_CODE':
                    # auth code is incorrect
                    raise InvalidAuthCodeException(e.name, e.desc) from e
                case 'invalid_grant':
                    # auth code has already been used
                    raise ExpiredAuthCodeException(e.name, e.desc) from e
                case 'INVALID_REDIRECT_URI':
                    # redirect given in auth_url doesn't match redirect on Yahoo
                    raise InvalidRedirectURIException(e.name, e.desc) from e


    def refresh_token(self, token):
        res = self.api_client.post(url=TOKEN_URL,
                                   data={'grant_type': 'refresh_token',
                                         'redirect_uri': self.redirect_uri,
                                         'refresh_token': token.refresh_token})
        token_json = json.loads(res.content)
        token.update(token_json)

    def get_valid_user_token(self, user_id):
        token = self.tokens.get(user_id)
        if token is None:
            # token has not been generated for user -> throw NotGeneratedException
            pass
        elif not token.is_valid():
            self.refresh_token(token)
        return token


class AuthException(Exception):
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc
        super().__init__(f'Authentication Error [{name}]:\n\t{desc}')


class InvalidAuthCodeException(AuthException):
    pass


class ExpiredAuthCodeException(AuthException):
    pass


class InvalidRedirectURIException(AuthException):
    pass 
