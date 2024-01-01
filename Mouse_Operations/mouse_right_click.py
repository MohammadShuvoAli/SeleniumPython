import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')

act = ActionChains(driver)
act.context_click(button).perform()

time.sleep(2)
driver.quit()