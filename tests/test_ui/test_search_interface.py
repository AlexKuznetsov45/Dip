import pytest
from pages.main_page import MainPage
from pages.locators import MAIN_PAGE
import allure


@pytest.mark.usefixtures("browser")
class TestPossibleTitlesAppear:

    @allure.feature("UI Тестирование")
    @allure.story("Появление блока 'Возможно, вы искали'")
    def test_possible_titles_appear(self, browser):
        """
        Проверка блока 'Возможно, вы искали' при вводе названия фильма.
        """
        main_page = MainPage(browser)

        with allure.step("Переход на главную страницу"):
            main_page.open_homepage()

        with allure.step("Ввожу текст в поле поиска"):
            main_page.input_search_query("Ма")  # Используем правильный метод

        with allure.step("Ожидание появления блока 'Возможно, вы искали'"):
            main_page.wait_for_dropdown_list()

        with allure.step("Проверка наличия текста 'Возможно, вы искали'"):
            possible_titles_block = main_page.find_element(
                *MAIN_PAGE["possible_titles_block"])
        assert "Возможно, вы искали" in possible_titles_block.text, \
            "Текст не появился."
