from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

# counting no. of rows columns in the table
rows = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
no_of_rows = len(rows)
print("No of Rows:", no_of_rows)

columns = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr/th')
no_of_columns = len(columns)
print("No of Columns:", no_of_columns)

# reading specific row and column data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print("specific row and column data: ", data, "\n")

# printing all rows and columns from table
# range (start, stop, step) # start and stop optional
for r in range(2, no_of_rows+1):
    for c in range(1, no_of_columns+1):
        table = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(table, end="      ")
    print()

# read data based on condition
# finding out book information written by "Mukesh"
for r in range(2, no_of_rows+1):
    author = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[' + str(r) + ']/td[2]').text
    if author == "Mukesh":
        book_name = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td[1]').text
        book_subject = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[' + str(r) + ']/td[3]').text
        book_price = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[' + str(r) + ']/td[4]').text
        print(book_name, author, book_subject, book_price)

driver.quit()