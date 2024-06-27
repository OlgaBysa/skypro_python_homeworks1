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

chrome.get("http://the-internet.herokuapp.com/entry_ad")

firefox.get("http://the-internet.herokuapp.com/entry_ad")

#В модальном окне нажмите на кнопку Сlose.


try:

   wait = WebDriverWait(driver, 10 )
      
   modal_window =wait.until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
   close_button = wait.until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal_footer")))
   close_button.click()
   sleep(2)

   
   
    
except Exception as ex:
    print(ex)
finally:

   chrome.quit()
   firefox.quit()


