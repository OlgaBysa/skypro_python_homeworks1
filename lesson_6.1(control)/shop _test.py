import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_purchase_in_online_store(browser):
    browser.get("https://www.saucedemo.com/")
    
    # Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Добавление товаров в корзину
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item_name in items_to_add:
        browser.find_element(By.XPATH, f"//div[text()='{item_name}']/following-sibling::div/button").click()
    
    # Переход в корзину
    browser.find_element(By.ID, "shopping_cart_container").click()
    
    # Оформление покупки
    browser.find_element(By.ID, "checkout").click()
    
    # Заполнение формы
    browser.find_element(By.ID, "first-name").send_keys("Olga")
    browser.find_element(By.ID, "last-name").send_keys("Test")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    browser.find_element(By.ID, "continue").click()
    
    # Чтение итоговой стоимости
    total_price = browser.find_element(By.CLASS_NAME, "summary_total_label").text
    
    assert total_price == "$58.29", f"Ожидаемая итоговая сумма: $58.29, Фактическая сумма: {total_price}"
