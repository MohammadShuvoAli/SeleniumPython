from selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=op)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://whatmylocation.com/")

driver.quit()