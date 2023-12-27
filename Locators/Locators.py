from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5000)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Searching element using ID, Name & Class Locator
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

# Counting no. of slides using find_elements
slides = driver.find_elements(By.CLASS_NAME, "nivo-control")
print(len(slides))      # 2 Slides

# counting no. of links available in homepage using TAG_NAME locator
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))   # 90 Links
driver.quit()

