import pytest
from pages.main_page import MainPage
from pages.movie_page import MoviePage
import allure


@pytest.mark.usefixtures("browser")
class TestFirstResultSelection:

    @allure.feature("UI Тестирование")
    @allure.story("Выбор первого результата поиска")
    def test_select_first_search_result(self, browser):
        """
        Проверка выбора первого результата поиска.
        """
        main_page = MainPage(browser)
        movie_page = MoviePage(browser)

        with allure.step("Переход на главную страницу"):
            main_page.open_homepage()

        with allure.step("Ввод в поле поиска название фильма 'Матрица'"):
            main_page.input_search_query("Матрица")

        with allure.step("Ожидание загрузки выпадающего списка"):
            main_page.wait_for_dropdown_list()  # Дожидаемся появления выпадающего списка

        with allure.step("Выбор первого результата поиска"):
            main_page.select_first_search_result()

        with allure.step("Проверка информации о выбранном фильме (заголовок и рейтинг)"):
            movie_title = movie_page.get_movie_title()
            assert "Матрица (1999)" in movie_title, "Заголовок фильма отличается от ожидаемого."

            movie_rating = movie_page.get_movie_rating()
            assert abs(movie_rating -
                       8.5) <= 0.1, "Рейтинг фильма отличается от ожидаемого."
