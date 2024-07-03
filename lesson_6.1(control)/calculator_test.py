import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = browser.find_element_by_css_selector("#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    keys_to_press = ["7", Keys.ADD, "8", Keys.EQUAL]
    result = "15"
    
    for key in keys_to_press:
        time.sleep(1)  # Ждем 1 секунду между нажатиями
        browser.find_element_by_id("send").send_keys(key)
    
    time.sleep(45)  # Ждем 45 секунд
    
    output = browser.find_element_by_id("result").text
    assert output == result, f"Ожидаемый результат: {result}, Фактический результат: {output}"
