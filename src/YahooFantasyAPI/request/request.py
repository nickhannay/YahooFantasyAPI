import httpx


class YfRequest:
    _client = None

    @classmethod
    def get_client(cls):
        if (cls._client is None):
            cls._client = httpx.Client()
        return cls._client


def make_request(url, method='GET', headers=None, data=None):
    client = YfRequest.get_client()
    req = client.build_request(
        method=method,
        url=url,
        headers=headers,
        data=data)
    res = client.send(req)
    return res


def set_base_url(base_url):
    client = YfRequest.get_client()
    client.base_url = base_url


def set_base_headers(headers):
    client = YfRequest.get_client()
    client.headers = headers
