import discord
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

URL = 'https://visa.vfsglobal.com/mar/fr/prt/login'
geckodriver_path = r'C:\Users\hp\Downloads\geckodriver-v0.34.0-win32\geckodriver.exe'  # Update with the correct GeckoDriver path
firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Update with the correct Firefox binary path
chrome_driver_path = r'C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe'  # Update with the correct ChromeDriver path
USER_EMAIL = 'azizbaalla02@gmail.com'
USER_PASSWORD = '1234Aziz@'


def gen_firefox_driver():
    try:
        # Initialize Firefox service with explicitly specified GeckoDriver path
        service = Service(geckodriver_path)
        service.start()

        # Specify Firefox binary location
        options = Options()
        options.binary_location = firefox_binary_path

        # Open the URL
        browser = webdriver.Firefox(service=service, options=options)
        return browser
    except Exception as e:
        print("Error in Firefox Driver: ", e)


def gen_chrome_driver():
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("user-agent={}".format(user_agent))
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True
                )
        return driver
    except Exception as e:
        print("Error in Chrome Driver: ", e)


# Generate the Firefox driver
firefox_driver = gen_firefox_driver()

# Navigate to the URL using Firefox driver
if firefox_driver:
    try:
        firefox_driver.get(URL)

        # Accept cookies
        time.sleep(10)
        accept_cookies = firefox_driver.find_element(By.ID, 'onetrust-reject-all-handler')
        accept_cookies.click()
        time.sleep(3)

        # Enter user email
        user_email = firefox_driver.find_element(By.ID, 'mat-input-0')
        user_email.click()
        user_email.send_keys(USER_EMAIL)
        time.sleep(3)

        # Enter user password and submit
        user_pass = firefox_driver.find_element(By.ID, 'mat-input-1')
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
            firefox_driver.quit()
        except NameError:
            pass  # browser

else:
    print("Firefox Driver not initialized properly.")

# Generate the Chrome driver
chrome_driver = gen_chrome_driver()

# Navigate to the URL using Chrome driver
if chrome_driver:
    try:
        chrome_driver.get("https://visa.vfsglobal.com/mar/en/prt/login")
        time.sleep(10)  # Wait for the page to load

        # Your other code goes here

    finally:
        # Close the browser window
        chrome_driver.quit()
else:
    print("Chrome Driver not initialized properly.")
