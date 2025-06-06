# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Page Object cho trang Home: https://demoqa.com
    """
    URL = "https://demoqa.com"

    # Locator cho các card trên trang chủ
    CARD_ELEMENTS = (By.XPATH, "//h5[text()='Elements']/ancestor::div[contains(@class,'card')]")
    CARD_FORMS    = (By.XPATH, "//h5[text()='Forms']/ancestor::div[contains(@class,'card')]")
    # Có thể bổ sung thêm: Alerts, Widgets, Interactions, v.v.

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """
        Mở trang chủ.
        """
        self.visit(self.URL)

    def click_elements_card(self):
        """
        Click vào card 'Elements' để vào trang Elements.
        """
        self.click(self.CARD_ELEMENTS)

    def click_forms_card(self):
        """
        Click vào card 'Forms' để vào trang Forms.
        """
        self.click(self.CARD_FORMS)
