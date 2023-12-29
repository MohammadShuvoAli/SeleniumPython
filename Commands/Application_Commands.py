from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")

print("Title: ", driver.title)
print("Current URL: ", driver.current_url)
print("Page Source: ", driver.page_source)

driver.quit()