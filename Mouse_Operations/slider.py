import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

slider = driver.find_element(By.XPATH, '//*[@id="slider"]/span')

print("Slider Location Before: ")
print(slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(slider, +100, 0).perform()

print("Slider Location After: ")
print(slider.location)

time.sleep(2)
driver.quit()