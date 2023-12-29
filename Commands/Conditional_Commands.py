from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/register")

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status: ", search_box.is_displayed())
print("Display Status: ", search_box.is_enabled())

radio_button = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print("Radio Button Before Click: ", radio_button.is_selected())
radio_button.click()
print("Radio Button After Click: ", radio_button.is_selected())


sleep(1)
driver.quit()