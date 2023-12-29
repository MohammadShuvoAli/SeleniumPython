from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver. maximize_window()
driver.implicitly_wait(5)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
print("Self:")
company_name = driver.find_element(By.XPATH, "//a[contains(text(), 'Zomato')]/self::a").text
print(company_name) # a is the child element
#sleep(1)

# parent
# td is the parent element
print("Parent:")
company_name = driver.find_element(By.XPATH, "//a[contains(text(), 'Zomato')]/parent::td").text
print(company_name) # parent td tag does not contain any value so, it will return its child's value "Zomato"
#sleep(1)

# child
# tr ancestor node, from ancestor we can access all child(td) nodes
print("Child:")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr/child::td")
print(len(company_name))
child = ""
for company in company_name:
    child += company.text + " "
print(child)
#sleep(1)


# Ancestor
print("Ancestor:")
# tr does not contain any value so it will return all of its child value [Whole ROW]
company_name = driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr").text
print(company_name)
#sleep(1)

# Descendant
print("Descendant:")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(), 'Zomato')]/ancestor::tr/descendant::*")
print(len(company_name)) #7
found = ""
for company in company_name:
    found += company.text + " "
print(found)
#sleep(1)

# Following
print("Following:")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(), 'Zomato')]/ancestor::tr/following::*")
print("No. of Nodes: ", len(company_name)) # 921
#sleep(1)

# Following-sibling
print("Following Sibling: ")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(), 'Zomato')]/ancestor::tr/following-sibling::*")
print("No. of Nodes: ", len(company_name)) # 90
#sleep(1)

# Preceding
print("Preceding: ")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(), 'Zomato')]/ancestor::tr/preceding::*")
print("No. of Nodes: ", len(company_name)) # 2913
#sleep(1)

# Preceding-Following
print("Preceding Following: ")
company_name = driver.find_elements(By.XPATH, "//a[contains(text(), 'Zomato')]/ancestor::tr/preceding-sibling::*")
print("No. of Nodes: ", len(company_name)) # 2913
sleep(1)

driver.quit()