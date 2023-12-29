from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

Explicate_Wait = WebDriverWait(driver, 10, poll_frequency=2) # explicate wait declaration
# if condition is false then it will wait for 10 seconds
# if the WebDriver cannot find the element immediately,
# it will continuously check for the presence of the element at intervals of 2 seconds until the maximum wait time of 10 seconds is reached.
# This polling mechanism allows the script to wait for the element to become available within the specified time frame.

driver.get("https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("Bangladesh")
driver.find_element(By.NAME, "q").submit()

search_result = Explicate_Wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Bangladesh']")))
search_result.click()

driver.quit()