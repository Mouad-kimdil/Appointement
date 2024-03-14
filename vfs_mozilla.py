import discord
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://visa.vfsglobal.com/mar/fr/prt/login'
geckodriver_path = r'C:\Users\hp\Downloads\geckodriver-v0.34.0-win32\geckodriver.exe'  # Update with the correct GeckoDriver path
firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Update with the correct Firefox binary path
USER_EMAIL = 'azizbaalla02@gmail.com'
USER_PASSWORD = '1234Aziz@'

# Initialize Firefox service with explicitly specified GeckoDriver path
service = Service(geckodriver_path)
service.start()

# Specify Firefox binary location
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary_path

try:
    # Open the URL
    browser = webdriver.Firefox(service=service, options=options)
    browser.get(URL)

    # Accept cookies
    time.sleep(10)
    accept_cookies = browser.find_element(By.ID, 'onetrust-reject-all-handler')
    accept_cookies.click()
    time.sleep(3)

    # Enter user email
    user_email = browser.find_element(By.ID, 'mat-input-0')
    user_email.click()
    user_email.send_keys(USER_EMAIL)
    time.sleep(3)

    # Enter user password and submit
    user_pass = browser.find_element(By.ID, 'mat-input-1')
    user_pass.click()
    user_pass.send_keys(USER_PASSWORD)
    user_pass.send_keys(Keys.ENTER)
    time.sleep(3)

    # Wait for manual intervention
    input("Press Enter to close the browser...")
except Exception as e:
    print("Error:", e)
finally:
    try:
        # Close the browser if defined
        browser.quit()
    except NameError:
        pass  # browser variable not defined, no need to quit
