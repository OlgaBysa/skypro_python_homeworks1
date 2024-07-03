import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    first_name = browser.find_element_by_id("first-name")
    first_name.send_keys("Иван")

    last_name = browser.find_element_by_id("last-name")
    last_name.send_keys("Петров")

    address = browser.find_element_by_id("address")
    address.send_keys("Ленина, 55-3")

    email = browser.find_element_by_id("email")
    email.send_keys("test@skypro.com")

    phone_number = browser.find_element_by_id("phone-number")
    phone_number.send_keys("+7985899998787")

    city = browser.find_element_by_id("city")
    city.send_keys("Москва")

    country = browser.find_element_by_id("country")
    country.send_keys("Россия")

    job_position = browser.find_element_by_id("job-position")
    job_position.send_keys("QA")

    company = browser.find_element_by_id("company")
    company.send_keys("SkyPro")

    submit_button = browser.find_element_by_id("submit")
    submit_button.click()

    time.sleep(2)  # Даем время для обработки данных

    # Проверка подсветки полей
    zip_code = browser.find_element_by_id("zip-code")
    assert "rgb(255, 0, 0)" in zip_code.value_of_css_property("border-color"), "Zip code не подсвечено красным"

    other_fields = [first_name, last_name, address, email, phone_number, city, country, job_position, company]
    for field in other_fields:
        assert "rgb(0, 128, 0)" in field.value_of_css_property("border-color"), f"Поле {field.get_attribute('id')} не подсвечено зеленым"
 