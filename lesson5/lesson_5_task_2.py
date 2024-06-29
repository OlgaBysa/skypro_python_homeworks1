from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

time = sleep(1)


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

#Откройте страницу

count = 0

chrome.get("http://uitestingplayground.com/dynamicid")

firefox.get("http://uitestingplayground.com/dynamicid")

#Кликните на синюю кнопку.

blue_button = chrome.find_element(
    "xpath", '//button[text() = "Button with Dynamic ID"]').click()

blue_button = firefox.find_element(
    "xpath", '//button[text() = "Button with Dynamic ID"]').click()

#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

try:

   for _ in range(3):

    blue_button = chrome.find_element(
    "xpath", '//button[text() = "Button with Dynamic ID"]').click()
    
    blue_button = firefox.find_element(
    "xpath", '//button[text() = "Button with Dynamic ID"]').click()
    print(f"Клик выполнен ({_ + 1}/3)")

    count = count + 1
    
    print(count)
except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


    




