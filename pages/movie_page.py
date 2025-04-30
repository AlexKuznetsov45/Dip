from .base_page import BasePage
from .locators import MOVIE_PAGE


class MoviePage(BasePage):
    """Класс страницы фильма."""

    def get_movie_title(self):
        """Возвращает заголовок фильма."""
        title_element = self.find_element(*MOVIE_PAGE["movie_title"])
        return title_element.text

    def get_movie_rating(self):
        """Возвращает рейтинг фильма."""
        rating_element = self.find_element(*MOVIE_PAGE["movie_rating"])
        raw_rating = rating_element.text
        # Конвертировать в float с точкой
        return float(raw_rating.replace(",", "."))
