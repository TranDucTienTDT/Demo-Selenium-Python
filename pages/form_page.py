# pages/form_page.py

import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FormPage(BasePage):
    """
    Page Object cho trang 'Practice Form': https://demoqa.com/automation-practice-form
    """
    URL = "https://demoqa.com/automation-practice-form"

    # Locators chính của các input trên form:
    INPUT_FIRST_NAME  = (By.ID, "firstName")
    INPUT_LAST_NAME   = (By.ID, "lastName")
    INPUT_EMAIL       = (By.ID, "userEmail")
    RADIO_GENDER_M    = (By.XPATH, "//label[@for='gender-radio-1']")
    RADIO_GENDER_F    = (By.XPATH, "//label[@for='gender-radio-2']")
    RADIO_GENDER_O    = (By.XPATH, "//label[@for='gender-radio-3']")
    INPUT_MOBILE      = (By.ID, "userNumber")

    DOB_INPUT         = (By.ID, "dateOfBirthInput")
    DOB_YEAR_SELECT   = (By.CLASS_NAME, "react-datepicker__year-select")
    DOB_MONTH_SELECT  = (By.CLASS_NAME, "react-datepicker__month-select")
    # Các ngày có thể có nhiều selector, ví dụ: (By.XPATH, "//div[contains(@class,'react-datepicker__day--015')]")
    DOB_DAY_15        = (By.XPATH, "//div[text()='15' and contains(@class,'react-datepicker__day')]")

    INPUT_SUBJECTS    = (By.ID, "subjectsInput")
    CHECKBOX_SPORTS   = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    CHECKBOX_READING  = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    CHECKBOX_MUSIC    = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

    UPLOAD_PICTURE    = (By.ID, "uploadPicture")
    INPUT_ADDRESS     = (By.ID, "currentAddress")

    STATE_DROPDOWN    = (By.ID, "state")
    STATE_NCR_OPTION  = (By.XPATH, "//div[text()='NCR']")
    CITY_DROPDOWN     = (By.ID, "city")
    CITY_DELHI_OPTION = (By.XPATH, "//div[text()='Delhi']")

    BUTTON_SUBMIT     = (By.ID, "submit")

    # Sau khi submit, một modal hiện ra:
    MODAL_TITLE       = (By.ID, "example-modal-sizes-title-lg")
    MODAL_TABLE       = (By.CLASS_NAME, "table-responsive")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.visit(self.URL)

    def fill_first_name(self, first_name: str):
        self.type_text(self.INPUT_FIRST_NAME, first_name)

    def fill_last_name(self, last_name: str):
        self.type_text(self.INPUT_LAST_NAME, last_name)

    def fill_email(self, email: str):
        self.type_text(self.INPUT_EMAIL, email)

    def select_gender(self, gender: str = "Male"):
        """
        gender: "Male", "Female" hoặc "Other"
        """
        if gender.lower() == "male":
            self.click(self.RADIO_GENDER_M)
        elif gender.lower() == "female":
            self.click(self.RADIO_GENDER_F)
        else:
            self.click(self.RADIO_GENDER_O)

    def fill_mobile(self, mobile: str):
        self.type_text(self.INPUT_MOBILE, mobile)

    def select_dob(self, year: str = "1990", month: str = "May", day: str = "15"):
        """
        Chọn ngày tháng năm sinh. Mặc định chọn 15 May 1990.
        """
        self.click(self.DOB_INPUT)
        # Chọn năm
        year_select = self.find(self.DOB_YEAR_SELECT)
        year_select.click()
        year_select.find_element(By.XPATH, f"//option[text()='{year}']").click()

        # Chọn tháng
        month_select = self.find(self.DOB_MONTH_SELECT)
        month_select.click()
        month_select.find_element(By.XPATH, f"//option[text()='{month}']").click()

        # Chọn ngày
        self.click((By.XPATH, f"//div[text()='{day}' and contains(@class,'react-datepicker__day')]"))

    def fill_subjects(self, subject: str):
        self.type_text(self.INPUT_SUBJECTS, subject + "\n")

    def select_hobbies(self, hobbies: list):
        """
        hobbies: list chứa bất kỳ "Sports", "Reading", "Music"
        """
        for hb in hobbies:
            if hb.lower() == "sports":
                self.click(self.CHECKBOX_SPORTS)
            elif hb.lower() == "reading":
                self.click(self.CHECKBOX_READING)
            elif hb.lower() == "music":
                self.click(self.CHECKBOX_MUSIC)

    def upload_picture(self, file_name: str):
        """
        file_name: Tên file trong thư mục 'fixtures' (ví dụ: "example.png")
        """
        fixture_path = os.path.join(os.getcwd(), "tests", "fixtures", file_name)
        self.find(self.UPLOAD_PICTURE).send_keys(fixture_path)

    def fill_address(self, address: str):
        self.type_text(self.INPUT_ADDRESS, address)

    def select_state_and_city(self, state: str = "NCR", city: str = "Delhi"):
        # Cuộn xuống để dropdown hiện
        self.scroll_into_view(self.STATE_DROPDOWN)
        self.click(self.STATE_DROPDOWN)
        # Chọn state
        self.find((By.XPATH, f"//div[text()='{state}']")).click()
        # Chọn city
        self.click(self.CITY_DROPDOWN)
        self.find((By.XPATH, f"//div[text()='{city}']")).click()

    def submit_form(self):
        # Scroll xuống để nút submit hiện
        self.scroll_into_view(self.BUTTON_SUBMIT)
        self.click(self.BUTTON_SUBMIT)

    def get_modal_title(self) -> str:
        return self.get_text(self.MODAL_TITLE)

    def get_result_table(self) -> str:
        """
        Trả về toàn bộ nội dung table (dạng text).
        Bạn có thể parse thêm để kiểm tra từng dòng.
        """
        return self.get_text(self.MODAL_TABLE)
