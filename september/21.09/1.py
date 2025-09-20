from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/scroll")


wait = WebDriverWait(driver, 10)
first_quote = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".quote")))

print(first_quote.text)