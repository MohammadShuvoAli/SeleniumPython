import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

country_list = driver.find_elements(By.XPATH, '//*[@id="select2-billing_country-results"]/li')
print(len(country_list))

# printing all country names from dropdown
for country in country_list:
    print(country.text)

# selecting a specific country from dropdown
for country in country_list:
    if country.text == "Bangladesh":
        country.click()
        break

time.sleep(5)
driver.quit()