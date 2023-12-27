from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.facebook.com')

# tag & id CSS Selector (Tag name is optional)
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('tag & id CSS Selector')
driver.find_element(By.CSS_SELECTOR, '#email').send_keys('tag & id CSS Selector')
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#email').clear()
sleep(1)

# tag & class CSS Selector (Tag name is optional)
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('tag & class CSS Selector')
driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('tag & class CSS Selector')
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.inputtext').clear()
sleep(1)

# tag & attribute CSS Selector (Tag name is optional)
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal_email"]').send_keys('tag & attribute selector')
driver.find_element(By.CSS_SELECTOR, '[data-testid="royal_email"]').send_keys('tag & attribute selector')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal_email"]').clear()
sleep(1)

# Tag, class and attribute CSS Selector
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid="royal_email"]').send_keys('Tag, class and attribute CSS Selector')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid="royal_email"]').clear()
sleep(1)

driver.quit()