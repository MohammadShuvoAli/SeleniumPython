from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver. maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")


# Absolute XPath
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[2]/form/input').send_keys('Apple')
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[2]/form/button').click()
sleep(3)
driver.back()

# Relative XPath
driver.find_element(By.XPATH, '//*[@id="small-searchterms"]').send_keys('Apple')
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
sleep(3)

driver.quit()