import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

days = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")

# printing checkbox length
print("Days Count: ", len(days))

# printing checkbox values
day_count = 1
for day in days:
    print('Day ', day_count, ':', day.get_attribute("value"))
    day_count += 1

# selecting a single checkbox
#days[2].click()

# clicking on all checkbox
#for day in days:
#    day.click()

# selecting multiple checkbox by choice
for day in days:
    weekname = day.get_attribute('id')
    if weekname == 'friday' or weekname == 'sunday' or weekname == 'thursday':
        day.click()

# select last 2 days
# range(5, 7)
# totatnumbecofelements-2=starting index
# for i in range (len(days)-2, len(days)):
#     days[i].click()

# Select first 2 days
# for i in range(len(days)):
#     if i<2:
#         days[i].click()


# clearing selected checkboxes
for day in days:
    if day.is_selected():
        day.click()

time.sleep(2)
driver.quit()
