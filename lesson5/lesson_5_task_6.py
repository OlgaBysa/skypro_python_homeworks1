from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

time = sleep(2)


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


#Откройте страницу

try:
   chrome.get(" http://the-internet.herokuapp.com/login")
   input_name = chrome.find_element(By.ID, "username").send_keys("tomsmith")
   sleep(2)
   input_pass =chrome.find_element(
      By.ID, "password").send_keys("SuperSerretPassword!")
   sleep(1)
   button = chrome.find_element(By.TAG_NAME, "button").click()
   sleep(2)


   firefox.get(" http://the-internet.herokuapp.com/login")
   input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
   sleep(2)
   input_pass = firefox.find_element(
      By.ID, "password").send_keys("SuperSerretPassword!")
   sleep(1)
   button = firefox.find_element(By.TAG_NAME, "button").click()
   sleep(2)



except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


