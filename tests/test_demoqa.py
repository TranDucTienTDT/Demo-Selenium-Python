
# -*- coding: utf-8 -*-
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver():
    """
    Fixture tạo một phiên bản Chrome headless duy nhất cho toàn bộ suite.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    # Nếu bạn muốn thấy trình duyệt chạy, bỏ comment dòng sau:
    # options.headless = False

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("DemoQA Homepage")
@allure.story("Navigate to Elements section")
def test_navigate_to_elements(driver):
    """
    Test positive: Mở trang chủ https://demoqa.com, click vào card 'Elements' và verify URL.
    """
    with allure.step("Mở DemoQA Homepage"):
        driver.get("https://demoqa.com")

    with allure.step("Click vào card 'Elements'"):
        # Tìm thẻ <h5> có text = "Elements", rồi lấy ancestor div có class 'card'
        elements_card = driver.find_element(
            By.XPATH,
            "//h5[text()='Elements']/ancestor::div[contains(@class, 'card')]"
        )
        elements_card.click()

    with allure.step("Verify URL chứa '/elements'"):
        assert "/elements" in driver.current_url, f"URL hiện tại: {driver.current_url}"


@allure.feature("DemoQA Homepage")
@allure.story("Negative test for non-existent element")
def test_negative_nonexistent_element(driver):
    """
    Test negative: Mở trang chủ, tìm một element không tồn tại và verify nó ném NoSuchElementException.
    """
    with allure.step("Mở DemoQA Homepage"):
        driver.get("https://demoqa.com")

    with allure.step("Thử tìm element không tồn tại"):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.ID, "this-id-does-not-exist")

@allure.feature("DemoQA Homepage")
@allure.story("Negative test for non-existent element")
def test_negative_nonexistent_element_2(driver):
    """
    Test negative: Mở trang chủ, tìm một element không tồn tại và verify nó ném NoSuchElementException.
    """
    with allure.step("Mở DemoQA Homepage"):
        driver.get("https://demoqa.com")

    with allure.step("Thử tìm element không tồn tại"):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.ID, "this-id-does-not-exist")