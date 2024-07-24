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

def test_purchase_in_online_store(browser):
    browser.get("https://www.saucedemo.com/")
    
    # Authentication
    username_input = browser.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys("standard_user")
    
    password_input = browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("secret_sauce")
    
    browser.find_element(By.ID, "login-button").click()
    
    # Adding items to the cart
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item_name in items_to_add:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item_label']/following-sibling::div/button"))
        )
        add_to_cart_button.click()
    
    # Proceed to the cart
    browser.find_element(By.ID, "shopping_cart_container").click()
    
    # Checkout
    browser.find_element(By.ID, "checkout").click()
    
    # Fill out the form
    browser.find_element(By.ID, "first-name").send_keys("Ольга")
    browser.find_element(By.ID, "last-name").send_keys("Журавлева")
    browser.find_element(By.ID, "postal-code").send_keys("357700")
    browser.find_element(By.CLASS_NAME, "cart_button").click()
    
    # Read the total price
    total_price_text = browser.find_element(By.CLASS_NAME, "summary_total_label").text
    total_price = float(total_price_text.replace("Total: $", ""))
    
    assert total_price == 58.29, f"Expected total price: $58.29, Actual total price: {total_price_text}"
