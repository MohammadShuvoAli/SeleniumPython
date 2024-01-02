import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd() # getting current path


def chrome_setup():
    # setting download location and changing setting for downloading PDF
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=ops)
    return driver


def edge_setup():
    # setting download location and changing setting for downloading PDF
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True} # have open bug from selenium only for pdf file
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(options=ops)
    return driver


def firefox_setup():
    ops = webdriver.FirefoxOptions()
    # setting preferences for disabling download dialog in firefox
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") # pdf is mime type of pdf file
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    # for not opening pdf file in browser
    ops.set_preference("pdfjs.disabled", True)
    # setting location where to download file
    ops.set_preference("browser.download.folderList",2) # 0-Desktop, 1-Download folder, 2-Desired Location
    ops.set_preference("browser.download.dir", location)

    driver = webdriver.Edge(options=ops)
    return driver

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
driver.maximize_window()

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(10)
driver.quit()