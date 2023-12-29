from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.daraz.com.bd/")
driver.get("https://www.foodpanda.com.bd/")

driver.refresh() # foodpanda
driver.back() # daraz
driver.forward() # foodpanda

driver.quit()
