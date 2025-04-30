import pytest
import requests
from common.api_client import ApiClient
from testdata import API_TOKEN


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(token=API_TOKEN)


@pytest.mark.negative
def test_search_films_with_incorrect_method(api_client):
    headers = {"X-API-KEY": API_TOKEN}
    payload = {"keyword": "мстители", "page": 1}
    response = requests.post(
        api_client.base_url, headers=headers, params=payload)
    assert response.status_code == 500
