from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

dropdown = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
dropdown.select_by_visible_text("France")
dropdown.select_by_value('japan')

# capture all options and print them
options = dropdown.options
print("Total Number of Options:", len(options))

for option in options:
    print("Value:",option.get_attribute("value")," InnerHTML:", option.text)

# selecting options without dropdown built-in functions
for option in options:
    if option.text == 'Brazil':
        option.click()
        break

driver.quit()