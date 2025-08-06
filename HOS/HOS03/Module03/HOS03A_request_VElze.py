# CS506 - HOS03 - Web Scraping and Spreadsheets
# Script 2 (accurate to HOS03 instructions): request.py 🌐

import requests

# 🎧 Dance tech history—pulling raw text from the web
res = requests.get('http://web.textfiles.com/computers/3dbasics.txt')

try:
    res.raise_for_status()
    print("Status Code:", res.status_code)
    print("Length of the text:", len(res.text))
    print(res.text[:103])  # Sample first 103 characters
except Exception as exc:
    print("Oh no: %s" % (exc))

# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with Python requests module [Large language model]. https://openai.com/chatgpt
