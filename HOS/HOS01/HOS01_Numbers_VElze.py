# CS506 – HOS01A – Introduction to Python Part 1
# Topic: Python Basics – Variables and Input

# --------------------------------------------
# Section 2: Variables, Data Types, and User Input
# --------------------------------------------

# Let's prompt for user input
name = input("\nWhat's your name? ")
food = input("What is your favorite food? ")
expression = "mee too"
print(f"Hello {name.title()}! Your favorite food is {food.lower()}. {expression.upper()}!")

# --------------------------------------------
# Section 3: Multiple Assignments
# --------------------------------------------
a = b = c = 10
x, y, z = 1, 2, 3
print("\nMultiple assignments:", a, b, c, x, y, z)

# --------------------------------------------
# Section 4: String Functions and Concatenation
# --------------------------------------------
message = "Python is FUN!"
print(message.title())
print(message.upper())
print(message.lower())
custom_message = f"{name}, welcome to CS506!"
print(custom_message)

# --------------------------------------------
# Section 5: Numbers and Operators (Numbers.py)
# --------------------------------------------
print("\nFloat")
a = 2.2
b = 2
c = 0.1
print("a + b =", a + b)
print("a + c =", a + c)
print("a * b =", a * b)
print("a ** b =", a ** b)

# --------------------------------------------
# End of HOS01A Script
# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Python basics and HOS01 tutorial [Large language model]. https://openai.com/chatgpt
