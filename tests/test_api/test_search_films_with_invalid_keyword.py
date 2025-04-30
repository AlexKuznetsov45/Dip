import pytest
import requests
from common.api_client import ApiClient
from testdata import API_TOKEN


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(token=API_TOKEN)


@pytest.mark.negative
def test_search_films_with_invalid_keyword(api_client):
    headers = {"X-API-KEY": API_TOKEN}
    payload = {"keyword": "!@#$%^&*()", "page": 1}
    response = requests.get(api_client.base_url,
                            headers=headers, params=payload)
    # Проверяем, что сервер возвращает успешный ответ
    assert response.status_code == 200
    assert len(response.json()["films"]) == 0  # Проверяем, что фильмов нет
