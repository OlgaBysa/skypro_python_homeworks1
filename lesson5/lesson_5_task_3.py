from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

time = sleep(1)


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


#Откройте страницу

chrome.get("http://uitestingplayground.com/classattr")

firefox.get("http://uitestingplayground.com/classattr")

#Кликните на синюю кнопку.

blue_button = chrome.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

blue_button = firefox.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

try:

   for _ in range(3):

    blue_button = chrome.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(2)

    
    blue_button = firefox.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(2)

    chrome.switch_to.accept()
    firefox.switch_to.accept()
    
except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


