import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

# counting no. of rows columns in the table
no_of_rows = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
print("No of Rows:",len(no_of_rows))

no_of_columns = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr/th')
print("No of Columns:",len(no_of_columns))

# reading specific row and column data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)


time.sleep(5)
driver.quit()