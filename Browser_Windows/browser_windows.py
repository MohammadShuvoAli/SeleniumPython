import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")

windowID = driver.current_window_handle
print("Window ID:",windowID)

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

windowIDs = driver.window_handles

for id in windowIDs:
    print(id)

parent_window_id = windowIDs[0]
child_window_id = windowIDs[1]

driver.switch_to.window(parent_window_id)
print("Parent Window:",driver.title)
time.sleep(5)

driver.switch_to.window(child_window_id)
print("Child Window:",driver.title)

print("\nPrinting using Loop")
for id in windowIDs:
    driver.switch_to.window(id)
    print(driver.title)

print("\nClosing a Specific window")
for id in windowIDs:
    driver.switch_to.window(id)
    if driver.title == 'OrangeHRM':
        driver.close()

time.sleep(5)
driver.quit()