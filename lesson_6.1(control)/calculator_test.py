import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    keys_to_press = ["7", Keys.ADD, "8", Keys.ENTER]
    result = "15"
    
    for key in keys_to_press:
        browser.find_element(By.CSS_SELECTOR, "#calculate").send_keys(key)  
    
    output = browser.find_element(By.CSS_SELECTOR, "#display").text 
    assert output == result, f"Expected result: {result}, Actual result: {output}"
