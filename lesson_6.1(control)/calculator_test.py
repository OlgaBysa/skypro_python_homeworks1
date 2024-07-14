import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_from(chrome_browser):
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)

    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()
    
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"

   

# def test_calculator_from(chrom_browser):
#     chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
#     delay_input.clear()
#     delay_input.send_keys(45)
#     chrom_browser.find_element(By.XPATH, "//span[text() = '7']").click()
#     chrom_browser.find_element(By.XPATH, "//span[text() = '+']").click()
#     chrom_browser.find_element(By.XPATH, "//span[text() = '8']").click()
#     chrom_browser.find_element(By.XPATH, "//span[text() = '=']").click()
    
#     WebDriverWait(chrom_browser,46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
#     result_text = chrom_browser.find_element(By.CLASS_NAME, "screen").text
#     assert result_text == "15"