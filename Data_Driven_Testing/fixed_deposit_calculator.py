import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from Excel_Read_Write import XLUtilities

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BS001.html")

popup_notification = driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]')
ad_popup = driver.find_element(By.XPATH, '//*[@id="Line_52"]')

if popup_notification.is_displayed():
    popup_notification.click()
elif ad_popup.is_displayed():
    ad_popup.click()

file = os.getcwd() + "\\caldata.xlsx"
rows = XLUtilities.getRowCount(file, "Sheet1")

for r in range(2, rows+1):
    principle_amount = XLUtilities.readData(file, "Sheet1", r, 1)
    rate_of_interest = XLUtilities.readData(file, "Sheet1", r, 2)
    period1 = XLUtilities.readData(file, "Sheet1", r, 3)
    period2 = XLUtilities.readData(file, "Sheet1", r, 4)
    frequency = XLUtilities.readData(file, "Sheet1", r, 5)
    expected_maturity_value = XLUtilities.readData(file, "Sheet1", r, 6) # getting as string value

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle_amount)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_of_interest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)

    period_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    period_dropdown.select_by_visible_text(period2)

    frequency_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]/img').click()

    actual_maturity_value = driver.find_element(By.XPATH, '//*[@id="resp_matval"]/strong').text # in string format

    # validation
    if float(expected_maturity_value) == float(actual_maturity_value):
        print("Test Passed!!!")
        XLUtilities.writeData(file, "Sheet1", r, 8, "Passed")
        XLUtilities.fillGreen(file, "Sheet1", r, 8)
    else:
        print("Test Failed!!!")
        XLUtilities.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtilities.fillRed(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
    time.sleep(2)

driver.quit()