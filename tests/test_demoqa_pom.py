# tests/test_demoqa_pom.py

import pytest
import allure
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.form_page import FormPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@allure.feature("DemoQA POM Tests")
class TestDemoQAPOM:

    @allure.story("Kiểm tra chức năng điều hướng từ Home → Elements")
    def test_navigate_to_elements(self, driver):
        step_num = 1
        with allure.step(f"Step {step_num}: Load Home Page"):
            home = HomePage(driver)
            home.load()
        step_num += 1
        with allure.step(f"Step {step_num}: Click Elements Card"):
            home.click_elements_card()
        step_num += 1
        with allure.step(f"Step {step_num}: Kiểm tra URL ElementsPage"):
            elements_page = ElementsPage(driver)
            assert "/elements" in elements_page.get_current_url(), \
            f"URL hiện tại không chứa '/elements': {elements_page.get_current_url()}"
            with pytest.raises(NoSuchElementException):
                home.find((By.ID, "element-khong-ton-tai"))
