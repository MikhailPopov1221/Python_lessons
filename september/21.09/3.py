from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


driver = webdriver.Firefox()

driver.get("https://practice.expandtesting.com/login")

input_username = driver.find_element(By.ID, "username")
input_password = driver.find_element(By.ID, "password")

input_username.clear()
input_password.clear()

input_username.send_keys("practice")
input_password.send_keys("SuperSecretPassword!")


login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

wait = WebDriverWait(driver, 15)
try:
    wait.until(expected_conditions.url_contains("/secure"))
    print("Успешный логин")
except Exception:
    print("Не удалось войти на сайт")
finally:
    time.sleep(15)
    driver.close()