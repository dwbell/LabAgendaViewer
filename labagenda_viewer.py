from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Web driver choice
driver = webdriver.Chrome('/home/pi/Python/LabAgendaViewer/chromedriver', chrome_options)
driver.maximize_window()

# Navigates to specified page, and waits for page load
driver.get('https://my.labagenda.com/index.php')

# Retrieve and initialize email element
email = driver.find_element_by_id("email")
email.clear()
email.send_keys('BalanceLabTV')

# Retrieve and initilize password element
password = driver.find_element_by_id("password")
password.clear()
password.send_keys('XXX')

# Submit user credentials to server
login = driver.find_element_by_xpath('//*[@id="login-box"]/div[4]/button')
login.click()

# Navigate to 'Machine Shop' page
driver.get('https://my.labagenda.com/schedule.php?sid=8642')

# Close resource filter
resourcefilter = driver.find_element_by_xpath('//*[@id="reservations-left"]/div[1]/a/i')
resourcefilter.click()

# Keep page refreshed
while(True):
    time.sleep(60)
    driver.refresh()

#driver.close()
