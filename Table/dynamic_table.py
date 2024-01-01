import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")

# Login to ORANGE HRM
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()

# Get all rows within the div
table_rows = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div')
table_columns = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div')
no_of_rows = len(table_rows)
no_of_columns = len(table_columns)
print("No of Rows:", no_of_rows)
print("No of Columns:", no_of_columns)

print("\nPrinting Table Data:")
for r in range(1, no_of_rows+1):
    for c in range(2, no_of_columns):
        table_data = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['+str(r)+']/div/div['+str(c)+']/div').text
        print(table_data, end='     ')
    print()

time.sleep(5)
driver.quit()