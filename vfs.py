import discord
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://visa.vfsglobal.com/mar/en/prt/login'
path = '/Users/hp/Downloads/chromedriver-win64/chromedriver.exe'
USER_EMAIL = 'azizbaalla02@gmail.com'
USER_PASSWORD = '1234Aziz@'

CHANNEL_ID = 1118858794299039744  # Replace with your Discord channel ID

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

driver_path = path
service = Service(driver_path)
browser = webdriver.Chrome(service=service)
browser.get(URL)
time.sleep(10)

accept_cookies = browser.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_cookies.click()
time.sleep(3)

user_email = browser.find_element(By.ID, 'mat-input-0')
user_email.click()
user_email.send_keys(USER_EMAIL)
time.sleep(3)

user_pass = browser.find_element(By.ID, 'mat-input-1')
user_pass.click()
user_pass.send_keys(USER_PASSWORD)
user_pass.send_keys(Keys.ENTER)
time.sleep(3)
#//*[@id="recaptcha-anchor"]/div[1]
iframe = browser.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
browser.switch_to.frame(iframe)
iframe.click()
time.sleep(10)

input("Press Enter to close the browser...")
browser.quit()
