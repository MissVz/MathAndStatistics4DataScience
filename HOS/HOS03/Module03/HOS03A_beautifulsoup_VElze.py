# CS506 - HOS03 - Web Scraping and Spreadsheets
# Script 3 (HOS03 version): beautifulsoup.py 🧼

import bs4
import requests

file = open("example.html")
lsoup = bs4.BeautifulSoup(file.read(), "html.parser")
elem = lsoup.select("#author")
print(elem[0].get_text())

import requests
import bs4

res = requests.get("http://www.cs.cmu.edu/~pausch/")
# used for display error message if url not valid
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

# store list of all <h1> tags to element
element = soup.select("h1")
for item in element:
    print(item)
    print(item.get_text())
    print()


# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with local HTML parsing using BeautifulSoup [Large language model]. https://openai.com/chatgpt
