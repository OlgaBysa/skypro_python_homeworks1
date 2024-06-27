from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()



chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    #Пять раз кликните на кнопку Add Element

for _ in range(5):

        add_button = chrome.find_element(
            By.XPATH, '//button[text() = "Add Element"]').click()
        
        add_button = firefox.find_element(
            By.XPATH, '//button[text() = "Add Element"]').click()
        
        sleep(5)

    #Соберите со страницы список кнопок Delete.

chrome_delete_button = chrome.find_elements(
        "xpath", '//button[text() = "Delete"]')
    
firefox_delete_button = firefox.find_elements(
        "xpath", '//button[text() = "Delete"]')
    
    
    #Выведите на экран размер списка.
print(
        f"{len(chrome_delete_button)}")

print(
        f"{len(firefox_delete_button)}")


chrome.quit()

firefox.quit()


        
        
        
