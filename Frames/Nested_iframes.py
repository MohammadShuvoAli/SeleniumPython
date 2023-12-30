import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outer_frame = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Shuvo")

time.sleep(1)

# driver.switch_to.parent_frame() # directly switch to parent frame (outer_frame)
# driver.switch_to.parent_frame() # directly switch to parent frame (main frame/page)
driver.switch_to.default_content() # going back to main frame
driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()

time.sleep(1)
driver.quit()