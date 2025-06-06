# pages/elements_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ElementsPage(BasePage):
    """
    Page Object cho trang 'Elements': https://demoqa.com/elements
    """
    URL = "https://demoqa.com/elements"

    # Ví dụ các locator trong trang Elements:
    OPTION_TEXT_BOX    = (By.XPATH, "//span[text()='Text Box']/ancestor::li")
    OPTION_CHECK_BOX   = (By.XPATH, "//span[text()='Check Box']/ancestor::li")
    OPTION_RADIO_BTN   = (By.XPATH, "//span[text()='Radio Button']/ancestor::li")
    OPTION_WEB_TABLE   = (By.XPATH, "//span[text()='Web Tables']/ancestor::li")
    OPTION_BUTTON      = (By.XPATH, "//span[text()='Buttons']/ancestor::li")
    OPTION_LINK        = (By.XPATH, "//span[text()='Links']/ancestor::li")
    # … bạn có thể bổ sung thêm các mục khác như Upload/Download, Dynamic Properties, v.v.

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """
        Mở thẳng trang Elements (nếu cần test trực tiếp mà không qua HomePage).
        """
        self.visit(self.URL)

    def click_text_box_option(self):
        self.click(self.OPTION_TEXT_BOX)

    def click_check_box_option(self):
        self.click(self.OPTION_CHECK_BOX)

    def click_radio_button_option(self):
        self.click(self.OPTION_RADIO_BTN)

    def click_web_tables_option(self):
        self.click(self.OPTION_WEB_TABLE)

    #… tương tự cho các option còn lại
