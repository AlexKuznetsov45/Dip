import pytest
from common.search_results_page import SearchResultsPage
from common.api_client import ApiClient
from testdata import API_TOKEN


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(token=API_TOKEN)


@pytest.fixture(scope="session")
def search_results_page(api_client):
    return SearchResultsPage(api_client)


@pytest.mark.positive
def test_search_films_by_keyword_with_valid_params(search_results_page):
    results = search_results_page.search_films(keyword="мстители", page=1)
    assert results["pagesCount"] >= 1  # Проверяем, что страниц достаточно
    assert len(results["films"]) > 0  # Проверяем, что есть фильмы на странице
