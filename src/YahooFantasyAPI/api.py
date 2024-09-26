import auth


class YFAPI:
    def __init__(self, client_id, client_secret, redirect_uri='oob'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def generate_auth_url(self):
        return auth.generate_url(self.client_id, self.redirect_uri)

    def generate_token(self, auth_code):
        auth_hash = auth.generate_hash(self.client_id, self.client_secret)
        return auth.generate_token(auth_code, auth_hash, self.redirect_uri)
    
    
