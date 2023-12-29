from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver. maximize_window()
driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/")


# Absolute XPath
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[2]/form/input').send_keys('Apple')
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[2]/form/button').click()
# sleep(3)
driver.back()

# Relative XPath
driver.find_element(By.XPATH, '//*[@id="small-searchterms"]').send_keys('Apple')
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
# sleep(3)

# XPath AND
driver.find_element(By.XPATH, "//input[@name='q' and @placeholder='Search store']").send_keys("XPath AND")
#sleep(3)
driver.find_element(By.XPATH, "//input[@name='q' and @placeholder='Search store']").clear()

# XPath OR
driver.find_element(By.XPATH, "//input[@name='q' or @placeholder='Search']").send_keys("XPath OR")
driver.find_element(By.XPATH, "//input[@name='q' or @placeholder='Search']").clear()
#sleep(3)

# Xpath contains()
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search')]").send_keys("XPath contains()")
# sleep(3)
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search')]").clear()

# XPath starts-with()
driver.find_element(By.XPATH, "//input[starts-with(@placeholder,'Sea')]").send_keys("XPath starts-with()")
#sleep(3)
driver.find_element(By.XPATH, "//input[starts-with(@placeholder,'Sea')]").clear()

# Xpath text()
driver.back()
driver.find_element(By.XPATH, "//a[text()='Build your own computer']").click()
sleep(2)
driver.back()
sleep(1)

driver.quit()