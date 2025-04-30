import requests


class ApiClient:
    def __init__(self, token=None):
        base_url = "https://kinopoiskapiunofficial.tech/api/v2.1/"
        self.base_url = base_url + "films/search-by-keyword"
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
            return requests.get(self.base_url, headers=self.headers,
                                params=params)
        elif method.upper() == "POST":
            return requests.post(self.base_url, headers=self.headers,
                                 params=params)
        else:
            error_message = f"Unsupported method: {method}"
            raise ValueError(error_message)
