import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
all_table_rows = []
all_table_columns = []

while True:
    try:
        # Get the current page's data
        table_rows = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div')
        table_columns = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div')
        all_table_rows.extend(table_rows)
        all_table_columns.extend(table_columns)

        # Get the "Next" button
        next_page = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[4]/nav/ul/li[3]/button/i')

        # Check if the number of rows exceeds a certain threshold (e.g., 50)
        if len(all_table_rows) > 50:
            break

        # Click the "Next" button
        next_page.click()

        # Sleep to allow the page to load
        time.sleep(2)
    except NoSuchElementException:
        break  # Break the loop if the "Next" button is not found

no_of_rows = len(all_table_rows)
no_of_columns = len(all_table_columns)
print("No of Rows:", no_of_rows)
print("No of Columns:", no_of_columns)

print("\nPrinting Table Data:")
for r in range(1, no_of_rows + 1):
    for c in range(2, no_of_columns):
        table_data = driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[' + str(r) + ']/div/div[' + str(c) + ']/div').text
        print(table_data, end='     ')
    print()

time.sleep(5)
driver.quit()
