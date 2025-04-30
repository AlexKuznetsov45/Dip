import pytest
from pages.main_page import MainPage
from pages.locators import MAIN_PAGE  # Импортируем локаторы
import allure


@pytest.mark.usefixtures("browser")
class TestTicketAndBuyThenCitySelect:

    @allure.feature("UI Тестирование")
    @allure.story("Выбор билета и затем выбор города")
    def test_click_ticket_and_buy_then_city(self, browser):
        """
        Проверка последовательного выбора билета и последующего выбора города:
        1. Перейти на страницу 'Билеты в кино'
        2. Выбрать фильм
        3. Нажать кнопку 'Купить билет'
        4. Выполнить клик по полю выбора города
        """
        main_page = MainPage(browser)

        with allure.step("Переход на главную страницу"):
            main_page.open_homepage()

        with allure.step("Клик по пункту меню 'Билеты в кино'"):
            main_page.click_tickets_menu()

        with allure.step("Клик по фильму"):
            # Новый локатор для фильма
            new_film_link = MAIN_PAGE["new_film_link"]
            main_page.click_element(*new_film_link)  # Используем новый локатор

        with allure.step("Клик по кнопке 'Купить билет'"):
            # Используем существующий метод
            main_page.click_element(*MAIN_PAGE["buy_ticket_button"])

        with allure.step("Клик по полю выбора города"):
            # Используем метод клика
            main_page.click_element(*MAIN_PAGE["city_select"])

        with allure.step("Проверка процесса выбора города"):
            # Тут можно добавить дополнительную проверку, например, наличие списка городов.
            pass
