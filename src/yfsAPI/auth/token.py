import time


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
