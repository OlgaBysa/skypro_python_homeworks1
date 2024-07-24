from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson7.constants import Test_from_URL
from Data_types.data import *

class MainPage:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get(Test_from_URL)

#Найти необходимые поля для заполнения на главной страницы

    def find_fields(self):
        self._first_name = (By.NAME, "first-name")
        self._last_name = (By.NAME, "last-name")
        self._address = (By.NAME, "address")
        self._email = (By.NAME, "e-mail")
        self._phone = (By.NAME, "phone")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._job_position = (By.NAME, "job-position")
        self._company = (By.NAME, "company")
        self._button = (By.TAG_NAME, "button")

#Заполняем найденные поля 

    def filling_in_the_fields(self):
        self.browser.find_element(*self._first_name).send_keys("first-name")
        self.browser.find_element(*self._last_name).send_keys("last-name")
        self.browser.find_element(*self._address).send_keys("address")
        self.browser.find_element(*self._email).send_keys("test@skypro.com")
        self.browser.find_element(*self._phone).send_keys("phone")
        # self.browser.find_element(*self._zip_code).send_keys("zip-code")
        self.browser.find_element(*self._city).send_keys("city")
        self.browser.find_element(*self._country).send_keys("coutry")
        self.browser.find_element(*self._job_position).send_keys("job-position")
        self.browser.find_element(*self._company).send_keys("company")
#Нажимаем на кнопку подтверждения

    def click_submit_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()