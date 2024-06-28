from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

time = sleep(2)


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


#Откройте страницу

try:
   chrome.get(" http://the-internet.herokuapp.com/login")
   chrome_input_name = chrome.find_element(By.ID, "username").send_keys("tomsmith")
   sleep(2)
   chrome_input_pass =chrome.find_element(
      By.ID, "password").send_keys("SuperSerretPassword!")
   sleep(1)
   chrome_button = chrome.find_element(By.TAG_NAME, "button").click()
   sleep(2)


   firefox.get(" http://the-internet.herokuapp.com/login")
   firefox_input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
   sleep(2)
   firefox_input_pass = firefox.find_element(
      By.ID, "password").send_keys("SuperSerretPassword!")
   sleep(1)
   firefox_button = firefox.find_element(By.TAG_NAME, "button").click()
   sleep(2)



except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


