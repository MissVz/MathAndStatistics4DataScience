# CS506 - HOS03 - Web Scraping and Spreadsheets
# Script 1 (accurate to HOS03 instructions): search_map.py 🗺️

import webbrowser
import sys

place = ''
if len(sys.argv) > 1:
    # 🪩 Getting the location straight from the command line—dance studio style
    place = ''.join(sys.argv[1:])  # Join without spaces, per HOS03 doc

# Open Google Maps using /search/ path
webbrowser.open("https://google.com/maps/search/" + place)

# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with Python webbrowser scripting [Large language model]. https://openai.com/chatgpt
