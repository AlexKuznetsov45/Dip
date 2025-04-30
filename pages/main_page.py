from .base_page import BasePage
from .locators import MAIN_PAGE, COMMON  # Импортируем локаторы


class MainPage(BasePage):
    """Класс главной страницы."""

    BASE_URL = "https://www.kinopoisk.ru/"

    def open_homepage(self):
        """Переход на главную страницу с ожиданием загрузки."""
        self.open_url(self.BASE_URL)
        # Ждём появления элемента на странице (например, поля поиска),
        # чтобы убедиться, что страница полностью загрузилась
        self.wait_until_visible(COMMON["search_field"])

    def perform_search(self, query):
        """Осуществляет поиск по заданному запросу."""
        self.clear_and_send_keys(*COMMON["search_field"], query)
        # Добавляем клик по кнопке "Фильтры"
        self.click_element(*MAIN_PAGE["filters_button"])

    def wait_for_search_results(self):
        """Ожидает появления блока с результатами поиска."""
        return self.find_element(*MAIN_PAGE["results_top_text"])

    def click_tickets_menu(self):
        """Клик по пункту меню 'Билеты в кино'."""
        self.click_element(*MAIN_PAGE["tickets_menu"])

    def click_film_link(self):
        """Клик по первой карточке фильма в результатах поиска."""
        self.click_element(*MAIN_PAGE["first_search_result"])

    def click_buy_ticket_button(self):
        """Клик по кнопке 'Купить билет'."""
        self.click_element(*MAIN_PAGE["buy_ticket_button"])

    def click_city_select(self):
        """Клик по полю выбора города."""
        self.click_element(*MAIN_PAGE["city_select"])

    def click_filters_button(self):
        """Клик по кнопке 'Фильтры'."""
        self.click_element(*MAIN_PAGE["filters_button"])

    def wait_for_filter_section(self):
        """Ожидает появления раздела с фильтрами."""
        return self.find_element(*MAIN_PAGE["filter_section"])

    def select_first_search_result(self):
        """Выбор первого результата поиска."""
        self.click_element(*MAIN_PAGE["first_search_result"])

    def input_search_query(self, query):
        """Ввод текста в поле поиска без нажатия кнопок."""
        search_field = self.find_element(*COMMON["search_field"])
        search_field.clear()  # Очищаем поле поиска
        search_field.send_keys(query)  # Вводим искомый текст

    def wait_for_dropdown_list(self):
        """Ожидание появления выпадающего списка после ввода текста в поиске."""
        self.wait_until_visible(MAIN_PAGE["dropdown_list"])
