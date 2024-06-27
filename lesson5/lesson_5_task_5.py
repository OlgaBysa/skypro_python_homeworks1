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
   chrome.get(" http://the-internet.herokuapp.com/inputs")
   input_field = chrome.find_element(By.TAG_NAME, "input")
   input_field.send_keys("1000")
   sleep(2)
   input_field.clear()
   sleep(1)
   input_field.send_keys("999")
   sleep(2)


   firefox.get(" http://the-internet.herokuapp.com/inputs")
   input_field = firefox.find_element(By.TAG_NAME, "input")
   input_field.send_keys("1000")
   sleep(2)
   input_field.clear()
   sleep(1)
   input_field.send_keys("999")
   sleep(2)



except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


