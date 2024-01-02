import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://mdbootstrap.com/docs/b4/jquery/plugins/file-upload/")

file_path = r"C:\Users\Shuvo\Desktop\sample.pdf"
driver.find_element(By.XPATH, "//input[@id='input-file-now']").send_keys(file_path)

time.sleep(5)
driver.quit()