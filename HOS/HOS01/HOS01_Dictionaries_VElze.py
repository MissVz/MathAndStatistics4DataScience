# CS506 – HOS01A – Introduction to Python Part 1
# Topic: Python Basics – Loops and Dictionaries

# --------------------------------------------
# Section 8: Dictionary Data Type (dictionary.py and compare.py)
# --------------------------------------------
print("\nDICTIONARY ACTIONS")
# Accessing
my_dict = {'Name': 'abc', 'Age': 7}
print("Name:", my_dict['Name'], "\nAge:", my_dict['Age'])

# Updating
my_dict['Age'] = 20
print("Updated Age:", my_dict['Age'])

# Adding
my_dict['Phone_no'] = 123456789
print("After adding the new pair:", my_dict)

# Deleting
del my_dict['Phone_no']
print("After deleting phone_no:", my_dict)

# Compare two lists
print("\nCOMPARISONS")
first = ['cats', 'dogs', 55]
second = ['dogs', 55, 'cats']
print(first)
print(second)
print("Are lists equal?", first == second, "\n")

# Compare two dictionaries, order does not matter
first_dict = {'name': 'aaa', 'species': 'human', 'age': 20}
second_dict = {'species': 'human', 'age': 20, 'name': 'aaa'}
print(first_dict)
print(second_dict)
print("Are dictionaries equal?", first_dict == second_dict)

# --------------------------------------------
# Section 9: Looping in Dictionary (dict_for.py and richest.py)
# --------------------------------------------
print("\nALIEN LOOPS!")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}

aliens = [alien_0, alien_1]

# Accessing key, value pairs in nested loop
for i in aliens:
    for key, value in i.items():
        print("KEY:", key, "\tVALUE:", value)

income = {
    'Alice': 90000,
    'Bob': 100000,
    'Jeff': 200000,
    'Apiwat': 999998,
    'Stark': 999999
}

print("\nMAX & MIN")
highest = max(income, key=income.get)
lowest = min(income, key=income.get)
print("The richest man on earth:", highest + ' with $' + str(income[highest]))
print("The least wealthy individual:", lowest + ' with $' + str(income[lowest]))

# --------------------------------------------
# End of HOS01A Script
# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Python basics and HOS01 tutorial [Large language model]. https://openai.com/chatgpt
