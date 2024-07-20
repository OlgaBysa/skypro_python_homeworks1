import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
      driver = webdriver.Chrome()
      yield driver
      driver.quit()

def test_fill_form(browser):
      browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
      browser.implicitly_wait(4)
      wait = WebDriverWait(browser, 20)  

      first_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
      first_name.send_keys("Иван")

      last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
      last_name.send_keys("Петров")

      address = wait.until(EC.visibility_of_element_located((By.ID, "address")))
      address.send_keys("Ленина, 55-3")

      email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
      email.send_keys("test@skypro.com")

      phone_number = wait.until(EC.visibility_of_element_located((By.ID, "phone-number")))
      phone_number.send_keys("+7985899998787")

      city = wait.until(EC.visibility_of_element_located((By.ID, "city")))
      city.send_keys("Москва")

      country = wait.until(EC.visibility_of_element_located((By.ID, "country")))
      country.send_keys("Россия")

      job_position = wait.until(EC.visibility_of_element_located((By.ID, "job-position")))
      job_position.send_keys("QA")

      company = wait.until(EC.visibility_of_element_located((By.ID, "company")))
      company.send_keys("SkyPro")

      submit_button = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
      submit_button.click()

      zip_code = wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))
      assert "denger" in zip_code.get_attribute("class")

      other_fields = browser.find_elements(By.CSS_SELECTOR, ".success")
      for field in other_fields:
          assert "success" in field.get_attribute("class")