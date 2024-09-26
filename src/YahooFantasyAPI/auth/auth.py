import time
import httpx
import base64
import json
from ..request import make_request

AUTH_URL = "https://api.login.yahoo.com/oauth2/request_auth"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"


def generate_url(client_id, redirect_uri='oob'):
    return f'{AUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&language=en-us'


def generate_token(auth_code, auth_hash, redirect_uri='oob'):
    res = make_request(url=TOKEN_URL,
                       method='POST',
                       headers={'Authorization': f'Basic {auth_hash}'},
                       data={'grant_type': 'authorization_code',
                             'redirect_uri': redirect_uri,
                             'code': auth_code})
    token_data = res.content
    token_json = json.loads(token_data)
    token = Token(token_json["access_token"], token_json["refresh_token"], token_json["expires_in"])
    return token


def generate_hash(client_id, client_secret):
    base_string_bytes = f'{client_id}:{client_secret}'.encode()
    hash_encoded = base64.b64encode(base_string_bytes)
    return hash_encoded.decode()


def refresh_token(token, auth_hash, redirect_uri='oob'):
    client = httpx.Client()
    req = client.build_request(
        method='POST',
        url=TOKEN_URL,
        data={'grant_type': 'refresh_token',
               'redirect_uri': redirect_uri,
               'refresh_token': token.refresh_token},
        headers={
            'Authorization': f'Basic {auth_hash}'
        }
    )
    res = client.send(req)
    data = res.text
    token_json = json.loads(data)
    token.update(token_json)


class Token:
    def __init__(self, access_token, r_token, expires_in):
        self.access_token = access_token
        self.refresh_token = r_token
        self.expires_in = expires_in
        self.created_at = time.time()

    def __str__(self):
        return f'access_token: {self.access_token}\nrefresh_token: {self.refresh_token}\nexpires_in: {self.expires_in}\ncreated_at: {self.created_at}'

    def is_valid(self):
        return ((self.created_at + self.expires_in) < time.time())

    def update(self, token_data):
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data["refresh_token"]
        self.expires_in = token_data["expires_in"]
        self.created_at = time.time()
