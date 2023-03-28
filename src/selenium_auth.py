from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

# get pass and user in .env file
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
ssid = os.getenv("SSID")
site = os.getenv("SITE")

print(f"username {username}, password {password}, ssid {ssid}, site {site}," )

# Enter your wifi username and password here
#username = "enter your username"
#password = "enter your password"
#ssid =  "enter your ssid"
#site = "enter your site"

result = os.popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep -e '^\s*SSID' | sed 's/.*: //g'").read().splitlines()[0]
if result == ssid:
        
    # Set up the browser driver (assuming you have already downloaded the driver and put it in your PATH)
    driver = webdriver.Chrome(executable_path='./src/chromedriver')

    # Navigate to the login page
    driver.get(site)

    # Find and click the "Oturumu Aç" button
    auth_button = driver.find_element_by_xpath("//button[@onclick=\"location.href='http://10.254.0.254:1000/login?'\"]")
    auth_button.click()

    # Wait for the page to load
    time.sleep(1)

    # Find the username and password fields and fill them in
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(1)

    # Close the browser
    driver.quit()
else:
    sys.exit(0)