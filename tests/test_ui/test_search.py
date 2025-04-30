import pytest
from pages.main_page import MainPage
from pages.locators import COMMON, MAIN_PAGE  # Импортируем локаторы
import allure


@pytest.mark.usefixtures("browser")
class TestSearchInterface:

    @allure.feature("UI Тестирование")
    @allure.story("Проверка интерфейса поиска")
    def test_search_interface_works_correctly(self, browser):
        """
        Проверка доступности и правильности работы интерфейса поиска.
        """
        main_page = MainPage(browser)

        with allure.step("Переход на главную страницу"):
            main_page.open_homepage()

        with allure.step("Ожидаю появления поля поиска"):
            # локатор для поля поиска
            main_page.find_element(*COMMON["search_field"])

        with allure.step("Ввожу текст в поле поиска"):
            main_page.input_search_query("Матрица")  # метод для ввода текста

        with allure.step("Нажимаю кнопку 'Найти'"):
            # Клик по кнопке "Найти"
            main_page.click_element(*MAIN_PAGE["submit_button"])

        with allure.step("Жду появления результатов поиска"):
            # метод для ожидания результатов
            search_results = main_page.wait_for_search_results()

        with allure.step("Проверяю наличие результата поиска"):
            result_text = search_results.text
            assert "Матрица" in result_text, "Название фильма отсутствует среди результатов поиска!"
            assert "результаты:" in result_text, "Количество результатов не отображается!"
