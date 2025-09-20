from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

time.sleep(30)

driver.quit()