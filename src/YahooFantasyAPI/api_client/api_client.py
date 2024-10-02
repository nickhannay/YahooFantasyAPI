import httpx


class APIClient:
    def __init__(self, base_url=None, base_headers=None):
        self.http_client = httpx.Client()
        if base_url is not None:
            self.http_client.base_url = base_url
        if base_headers is not None:
            self.http_client.headers = base_headers

    def get(self, url, headers=None):
        res = self.http_client.get(url=url,
                                   headers=headers)
        return res

    def post(self, url, headers=None, data=None):
        res = self.http_client.post(url=url,
                                    headers=headers,
                                    data=data)
        return res
    
