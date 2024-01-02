from selenium import webdriver


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver


def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver


def headless_firefox():
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver

driver = headless_chrome()
# driver = headless_edge()
# driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)

driver.quit()