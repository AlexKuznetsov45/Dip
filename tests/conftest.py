# conftest.py
import pytest
from selenium import webdriver
from common.api_client import ApiClient
from common.search_results_page import SearchResultsPage
from testdata import API_TOKEN  # Импортируем токен из testdata.py

# Фикстура для браузера (для UI-тестов)


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура для API (для API-тестов)


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(token=API_TOKEN)  # Берем токен из файла testdata.py


@pytest.fixture(scope="session")
def search_results_page(api_client):
    return SearchResultsPage(api_client)

# Регистрация маркеров "positive" и "negative"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "positive: Mark test as positive scenario"
    )
    config.addinivalue_line(
        "markers",
        "negative: Mark test as negative scenario"
    )
