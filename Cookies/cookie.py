from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# capture cookie from browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# print details of all cookies
for cookie in cookies:
    print(cookie)

# print specific details from cookies
for cookie in cookies:
    print(cookie.get('name'), ",", cookie.get('value'))

# add new cookie to browser
driver.add_cookie({"name": "Shuvo", "value": "123456"})
cookies = driver.get_cookies()
print(len(cookies))
for cookie in cookies:
    print(cookie.get('name'), ",", cookie.get('value'))

# delete a specific cookie
driver.delete_cookie("Shuvo")
cookies = driver.get_cookies()
print(len(cookies))

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

driver.quit()