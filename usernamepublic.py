import random
import string
import requests
import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException

TOKEN = "bot token for sending messages to discord channel"
CHANNEL_ID = "discord channel id for sending messages about username status"
DISCORD_EMAIL = "for checking the availability of usernames"
DISCORD_PASSWORD = "for checking the availability of usernames"
COOKIES_FILE = "discord_cookies.pkl"

def dismiss_popups(driver):
    try:
        driver.switch_to.alert.dismiss()
    except:
        pass

def send_message(username, status):
    if status == "Username Free":
        color = 0x57F287
        title = "Username Available"
        description = f"`{username}` is available"
    else:
        color = 0xED4245
        title = "Username Taken"
        description = f"`{username}` is taken"

    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color,
        }]
    }
    requests.post(
        f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages",
        headers=headers,
        json=data
    )

def login_with_cookies(driver):
    if os.path.exists(COOKIES_FILE):
        print("Loading cookies...")
        driver.get("https://discord.com")
        time.sleep(2)
        cookies = pickle.load(open(COOKIES_FILE, "rb"))
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except:
                pass
        driver.refresh()
        time.sleep(4)
        if "channels" in driver.current_url or "app" in driver.current_url:
            print("Logged in with cookies!")
            return True
        print("Cookies expired!")
        return False
    return False

def manual_login(driver):
    print("=================================")
    print("Log in manually in the browser...")
    print("The script will continue automatically!")
    print("=================================")
    driver.get("https://discord.com/login")
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    try:
        email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email.send_keys(DISCORD_EMAIL)
        time.sleep(1)
        password = driver.find_element(By.NAME, "password")
        password.send_keys(DISCORD_PASSWORD)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        print("Credentials filled in, solve captcha if it appears...")
    except:
        print("Fill in manually...")

    wait2 = WebDriverWait(driver, 120)
    wait2.until(lambda d: "channels" in d.current_url or "app" in d.current_url)
    print("Logged in!")

    pickle.dump(driver.get_cookies(), open(COOKIES_FILE, "wb"))
    print("Cookies saved")

def popup_is_open(driver):
    try:
        field = driver.find_element(By.XPATH, "//input[@name='username']")
        return field.is_displayed()
    except:
        return False

def check_username(driver, username):
    global popup_open

    dismiss_popups(driver)

    try:
        if not popup_is_open(driver):
            popup_open = False

        if not popup_open:
            driver.get("https://discord.com/settings/account")
            time.sleep(6)
            dismiss_popups(driver)

            wait = WebDriverWait(driver, 15)
            wait.until(EC.presence_of_element_located((By.XPATH, "//button")))
            time.sleep(6)

            buttons = driver.find_elements(By.XPATH, "//button")
            for b in buttons:
                if b.text.strip() == "Edit":
                    b.click()
                    break
            time.sleep(6)
            popup_open = True

        wait = WebDriverWait(driver, 10)
        field = wait.until(EC.presence_of_element_located((By.XPATH,
            "//input[@name='username']"
        )))
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        time.sleep(0.3)
        field.send_keys(username)
        time.sleep(4)

        page = driver.page_source.lower()

        if "username is available" in page or "available. nice" in page:
            return "Username Free"
        else:
            return "Username Taken"

    except Exception as e:
        print(f"Error: {e}")
        popup_open = False
        return "Username Taken"

# Setup driver
options = Options()
options.add_argument("--lang=en-US")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {
    # Block protocol handler (first popup)
    "profile.default_content_setting_values.protocol_handlers": 2,
    "protocol_handler.excluded_schemes": {
        "discord": True,
        "discord-": True,
    },
    # Block "Save password?" (second popup)
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    # Block notifications
    "profile.default_content_setting_values.notifications": 2,
})

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

if not login_with_cookies(driver):
    manual_login(driver)

print("Starting search...")

popup_open = False

while True:
    username_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    username_digits = ''.join(random.choice(string.digits) for _ in range(4))

    status_letters = check_username(driver, username_letters)
    send_message(username_letters, status_letters)
    print(f"{username_letters} -> {status_letters}")

    status_digits = check_username(driver, username_digits)
    send_message(username_digits, status_digits)
    print(f"{username_digits} -> {status_digits}")

    time.sleep(1)