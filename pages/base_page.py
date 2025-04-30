from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц, содержит общие методы."""

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Переход на заданный URL."""
        self.driver.get(url)

    def find_element(self, by, locator, timeout=30):
        """Ожидание и возврат элемента по локатору."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def clear_and_send_keys(self, by, locator, text, timeout=30):
        """Очистка и ввод текста в элемент."""
        element = self.find_element(by, locator, timeout)
        element.clear()
        element.send_keys(text)

    def click_element(self, by, locator, timeout=30):
        """Ожидание и клик по элементу."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def wait_until_visible(self, locator, timeout=30):
        """Ожидание появления элемента на странице."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
