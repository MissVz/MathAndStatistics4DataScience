# CS506 – HOS05A: Headless Browser Automation
# Topic: Extracting a table from a website

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setup headless browser options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Optional fix to ignore Certificate and SSL errors
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# Launch the browser
driver = webdriver.Chrome(options=options)

# Load the target page
driver.get('https://www.w3schools.com/html/html_tables.asp')

# Locate the table
table = driver.find_element(By.ID, "customers")
rows = table.find_elements(By.TAG_NAME, "tr")

# Extract and print table data
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
    col_data = [col.text for col in cols]
    print(col_data)

# Close the browser
driver.quit()

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Selenium table scraping [Large language model]. https://openai.com/chatgpt
