# CS506 - HOS02 - Introduction to Python Pt 2
# Topic: Looping in Dictionary

income = {
    'Alice': 90000,
    'Bob': 100000,
    'Jeff': 200000,
    'Apiwat': 999998,
    'Stark': 999999
}

highest = max(income, key=income.get)
print("The richest man on earth:", end=' ')
print(highest + ' with $' + str(income[highest]))


# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with Python List Remove operations [Large language model]. https://openai.com/chatgpt
