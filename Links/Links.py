from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# click on link
links = driver.find_elements(By.XPATH, '//a')
print("Total Links Available on Page: ", len(links))

# print all link names
link_count = 1
for link in links:
    print("Link No.",link_count,'Name:', link.text)
    link_count += 1

driver.quit()
