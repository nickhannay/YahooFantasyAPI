import httpx
import json


class APIClient:
    def __init__(self, base_url=None, base_headers=None):
        self.http_client = httpx.Client()
        if base_url is not None:
            self.http_client.base_url = base_url
        if base_headers is not None:
            self.http_client.headers = base_headers

    def get(self, url, headers=None):
        return self.request('GET', url, headers)
        
    def post(self, url, headers=None, data=None):
        return self.request('POST', url, headers, data)
         
    def request(self, method, url, headers=None, data=None):
        req = self.http_client.build_request(
            method=method,
            url=url,
            headers=headers,
            data=data
        )
        try:
            res = self.http_client.send(req)
            res.raise_for_status()
            return res
        except httpx.RequestError as e:
            raise APIClientException(f'{e}') from e
        except httpx.HTTPStatusError as e:
            res = json.loads(e.response.content)
            exc = APIRequestException(res['error'], res['error_description'])
            raise exc from e
    


class APIClientException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f'Request to external Yahoo API failed:\n\t{msg}')


class APIRequestException(Exception):
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc
        super().__init__(f'Request Error - {name}:\n\t{desc}')