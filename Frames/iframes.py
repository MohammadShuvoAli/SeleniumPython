import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame('SingleFrame')
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Shuvo")

driver.switch_to.default_content() # going back to main frame
driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()

time.sleep(10)
driver.quit()