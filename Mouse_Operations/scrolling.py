import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://flagpedia.net/index")

# 1. scroll down by pixel
driver.execute_script("window.scrollBy(0, 3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)

# 2. scroll down till the element is visible
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of Bangladesh']")
driver.execute_script("arguments[0].scrollIntoView()", flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)

# 3. scroll down till the end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)

# 4. scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)

time.sleep(2)
driver.quit()