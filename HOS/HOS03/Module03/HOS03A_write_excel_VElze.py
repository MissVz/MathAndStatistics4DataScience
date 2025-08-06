# CS506 - HOS03 - Web Scraping and Spreadsheets
# Script 5: read_excel.py 📊
# Purpose: Read and format data from an Excel spreadsheet

import openpyxl

wb = openpyxl.Workbook()          # Create a new workbook
sheet = wb.active                 # Access the default sheet
sheet.title = "Cars"              # Rename the sheet
sheet['A1'] = "Models"            # Write header in A1
sheet['B1'] = "Price"             # Write header in B1

cars = [('BMW', 40000), ('Audi', 50000), ('Ford', 25000),
        ('McLaren', 1800000), ('Toyota', 30000)]

for car in cars:
    sheet.append(car)            # Append rows below the headers
    
wb.save("car_data.xlsx")          # Save workbook to file

# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with openpyxl spreadsheet reading [Large language model]. https://openai.com/chatgpt
