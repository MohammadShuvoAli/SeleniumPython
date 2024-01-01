import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)

# Date Format: DD/MM/YY
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("09/05/2024")

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

date = "5"
month = "September"
year = "2024"

while True:
    m = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    y = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    if month == m and year == y:
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click() # Next Button
        # driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click()  # Previous Button

dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for day in dates:
    if day.text == date:
        day.click()
        break

time.sleep(5)
driver.quit()