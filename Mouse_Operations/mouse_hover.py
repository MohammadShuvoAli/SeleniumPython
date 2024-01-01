import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

Computers = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
Electronics = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
Apparel = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Apparel']")
Accessories = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Accessories']")

act = ActionChains(driver)

# Mouse Hover
# perform() is mandatory for executing the action. without perform() it will just create the actionchain
act.move_to_element(Computers).move_to_element(Electronics).move_to_element(Apparel).move_to_element(Accessories).click().perform()

time.sleep(2)
driver.quit()