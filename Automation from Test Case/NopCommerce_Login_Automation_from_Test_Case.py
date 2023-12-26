from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")

driver.find_element(By.CLASS_NAME, "login-button").click()

expected_title = "Dashboard / nopCommerce administration"
actual_title = driver.title

if expected_title == actual_title:
    print("Test Successful!!!")
else:
    print("Test Failed!!!")

driver.close()


