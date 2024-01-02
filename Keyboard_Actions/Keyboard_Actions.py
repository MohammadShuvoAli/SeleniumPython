import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://text-compare.com/")

field1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
field2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

field1.send_keys("Hi! I am Shuvo")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(2)
driver.quit()