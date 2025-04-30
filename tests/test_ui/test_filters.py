import pytest
from pages.main_page import MainPage
from pages.locators import MAIN_PAGE  # Подключаем локаторы
import allure


@pytest.mark.usefixtures("browser")
class TestFiltersButtonClick:

    @allure.feature("UI Тестирование")
    @allure.story("Проверка кнопки 'Фильтры'")
    def test_filters_button_click(self, browser):
        """
        Проверка доступности и реакции кнопки 'Фильтры'.
        """
        main_page = MainPage(browser)

        with allure.step("Переход на главную страницу"):
            main_page.open_homepage()

        with allure.step("Нажимаю кнопку 'Фильтры'"):
            main_page.click_filters_button()

        with allure.step("Проверяю, что раздел с фильтрами отображается"):
            filters_section = main_page.find_element(
                *MAIN_PAGE["filter_section"])
            assert filters_section.is_displayed(), "Раздел не отображается!"
