import discord
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
URL = 'https://visa.vfsglobal.com/mar/en/prt/login'
USER_EMAIL = 'azizbaalla02@gmail.com'
USER_PASSWORD = '1234Aziz@'
CHANNEL_ID = 1118858794299039744  # Replace with your Discord channel ID

# Discord client setup
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Chrome WebDriver setup
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver_path = '/Users/hp/Downloads/chromedriver-win64/chromedriver.exe'
service = Service(driver_path)
browser = webdriver.Chrome(service=service, options=chrome_options)

# Login function
def login():
    browser.get(URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click() # Wait until the cookie accept button is clickable
    browser.find_element(By.ID, 'mat-input-0').send_keys(USER_EMAIL) # Fill in email
    browser.find_element(By.ID, 'mat-input-1').send_keys(USER_PASSWORD + Keys.RETURN) # Fill in password and submit

# ReCAPTCHA solving function
def solve_recaptcha():
    try:
        WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']"))) # Switch to reCAPTCHA iframe
        browser.find_element(By.ID, "recaptcha-anchor").click() # Click on the reCAPTCHA checkbox
    except NoSuchElementException:
        print("reCAPTCHA not found.")
    except ElementNotInteractableException:
        print("reCAPTCHA checkbox not interactable.")
    except ElementClickInterceptedException:
        print("reCAPTCHA checkbox click intercepted.")

# Discord message function
async def send_message():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Website login completed.")

# Main function
async def main():
    login()
    solve_recaptcha()
    await send_message()
    input("Press Enter to close the browser...")
    browser.quit()

# Discord event: on_ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Discord event: on_message
@client.event
async def on_message(message):
    if message.content.startswith('!login'):
        await main()

# Run the Discord client
client.run(os.environ['DISCORD_TOKEN'])
