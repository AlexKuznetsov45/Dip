import requests


class ApiClient:
    def __init__(self, token=None):
        self.base_url = "https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword"
        self.headers = {}
        if token:
            self.headers.update({"X-API-KEY": token})

    def send_request(self, keyword=None, page=None, method="GET"):
        params = {}
        if keyword:
            params['keyword'] = keyword
        if page:
            params['page'] = page

        if method.upper() == "GET":
            return requests.get(self.base_url, headers=self.headers, params=params)
        elif method.upper() == "POST":
            return requests.post(self.base_url, headers=self.headers, params=params)
        else:
            raise ValueError(f"Unsupported method: {method}")
