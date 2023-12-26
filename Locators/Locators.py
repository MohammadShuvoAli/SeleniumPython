from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5000)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Searching elements using ID, Name & Class Locator
driver.find_element(By.ID, "small-searchterms").clear()
driver.find_element(By.NAME, "q").send_keys("Apple")
driver.find_element(By.CLASS_NAME, "search-box-button").click()
print("Button Pressed")

# Going Back to Homepage
driver.back()

# Finding Element using link text
driver.find_element(By.LINK_TEXT, 'Build your own computer').click()
# Going Back to Homepage
driver.back()


# Finding element using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'HTC').click()
driver.back()


driver.quit()

