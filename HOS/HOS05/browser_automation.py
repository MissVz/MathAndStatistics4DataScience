# CS506 – HOS05A: Headless Browser Automation
# Topic: Taking a screenshot

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
print("Title of the page:", driver.title)

# Save a screenshot
driver.save_screenshot("screenshot.png")
driver.quit()

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Selenium headless browser automation [Large language model]. https://openai.com/chatgpt
