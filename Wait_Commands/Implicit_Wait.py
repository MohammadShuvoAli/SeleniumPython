from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# Specifies the maximum amount of time the WebDriver should wait when trying to find an element.
driver.implicitly_wait(5)

driver.get("https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("Bangladesh")
driver.find_element(By.NAME, "q").submit()
driver.find_element(By.XPATH, "//h3[normalize-space()='Bangladesh']").click()

driver.quit()
