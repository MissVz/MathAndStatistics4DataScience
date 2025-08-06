# CS506 – HOS01A – Introduction to Python Part 1
# Topic: Python Basics – Conditionals

# --------------------------------------------
# Section 6: Decision Making (If_ElIf_Control.py)
# --------------------------------------------
import random

# Prompt for user age first
age = int(input("Enter your age: "))
if age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
else:
    print("You're an adult.")

# Then play the guessing game without a loop
secret = random.randint(1, 6)
guess = int(input("Please guess an integer between 1 and 6: "))
if guess == secret:
    print("Congrats, you got it!")
elif guess < secret:
    print("Too low.")
else:
    print("Too high.")

if guess != secret:
    print(f"The correct number was {secret}.")
# --------------------------------------------
# End of HOS01A Script
# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Python basics and HOS01 tutorial [Large language model]. https://openai.com/chatgpt
