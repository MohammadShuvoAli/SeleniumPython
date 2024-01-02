import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd() # getting current path


def chrome_setup():
    preferences = {"download.default_directory":location} # setting download location
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=ops)
    return driver


def edge_setup():
    preferences = {"download.default_directory":location} # setting download location
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(options=ops)
    return driver


def firefox_setup():
    ops = webdriver.FirefoxOptions()
    # setting preferences for disabling download dialog in firefox
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword") # msword mime type
    ops.set_preference("browser.download.manager.showWhenStarting", False)

    # setting location where to download file
    ops.set_preference("browser.download.folderList",2) # 0-Desktop, 1-Download folder, 2-Desired Location
    ops.set_preference("browser.download.dir", location)

    driver = webdriver.Edge(options=ops)
    return driver

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.maximize_window()

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(2)
driver.quit()