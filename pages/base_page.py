# pages/base_page.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Lớp base chung cho tất cả các Page Object.
    """
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def visit(self, url: str):
        """
        Mở URL truyền vào.
        """
        self.driver.get(url)

    def find(self, locator: tuple):
        """
        Chờ cho đến khi element xuất hiện, rồi return WebElement.
        locator: (By.<METHOD>, "value")
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator: tuple):
        """
        Chờ ít nhất 1 element xuất hiện, rồi return list WebElements.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple):
        """
        Chờ element clickable rồi click.
        """
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def type_text(self, locator: tuple, text: str):
        """
        Chờ element visible, sau đó clear và send_keys.
        """
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """
        Lấy text của element sau khi chờ element visible.
        """
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        return elem.text

    def scroll_into_view(self, locator: tuple):
        """
        Scroll element vào view (sử dụng JS).
        """
        elem = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        time.sleep(0.5)

    def get_current_url(self) -> str:
        return self.driver.current_url
