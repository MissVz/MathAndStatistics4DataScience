# CS506 - HOS03 - Web Scraping and Spreadsheets
# Script 4: automate_web.py 🤖
# Purpose: Use Selenium to simulate user input on Google's signup form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # for dropdowns
from selenium.webdriver.support.ui import WebDriverWait  # for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # for wait conditions
import time

browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signup")

# Fill First Name
firstname = browser.find_element(By.ID, 'firstName')
firstname.send_keys('Thomas')
time.sleep(2)

# Fill Last Name
lastname = browser.find_element(By.ID, 'lastName')
lastname.send_keys("Anderson")
time.sleep(2)

# Click "Next"
browser.find_element(By.ID, "collectNameNext").click()
time.sleep(2)

# Fill Date of Birth
day = browser.find_element(By.NAME, "day")
day.send_keys('1')
time.sleep(2)

# Select Month
month = Select(browser.find_element(By.ID, "month"))
month.select_by_visible_text('January')
time.sleep(2)

# Fill Year
year = browser.find_element(By.NAME, "year")
year.send_keys("1990")
time.sleep(2)

# Select Gender
gender = Select(browser.find_element(By.ID, "gender"))
gender.select_by_visible_text("Male")
time.sleep(2)

# Click "Next"
browser.find_element(By.ID, "birthdaygenderNext").click()
time.sleep(2)

# Enter Username
username = browser.find_element(By.NAME, "Username")
username.send_keys("thomasanderson11990")
time.sleep(2)

# Click "Next"
browser.find_element(By.ID, "next").click()
time.sleep(2)

# Wait for password fields to appear
passwd = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
passwd.send_keys("ThomAnd1190")
time.sleep(2)

passwdAgain = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "PasswdAgain")))
passwdAgain.send_keys("ThomAnd1190")
time.sleep(2)

browser.find_element(By.ID, "createpasswordNext").click()
time.sleep(3)

# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with Selenium automation scripting [Large language model]. https://openai.com/chatgpt
