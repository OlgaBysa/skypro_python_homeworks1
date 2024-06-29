from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep




driver = webdriver.Chrome()

time = sleep(2)


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


#Откройте страницу

try:
   chrome.get(" http://the-internet.herokuapp.com/inputs")
   chrome_input_field = chrome.find_element(By.TAG_NAME, "input")
   chrome_input_field.send_keys("1000")
   sleep(2)
   chrome_input_field.clear()
   sleep(1)
   chrome_input_field.send_keys("999")
   sleep(2)


   firefox.get(" http://the-internet.herokuapp.com/inputs")
   firefox_input_field = firefox.find_element(By.TAG_NAME, "input")
   firefox_input_field.send_keys("1000")
   sleep(2)
   firefox_input_field.clear()
   sleep(1)
   firefox_input_field.send_keys("999")
   sleep(2)



except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


