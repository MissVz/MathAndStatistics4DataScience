# CS506 – HOS01A – Introduction to Python Part 1
# Topic: Python Basics – Loops and Lists

# --------------------------------------------
# Section 7: Using Loops in Lists (replaceNegative.py)
# --------------------------------------------
import random

# For Loop that runs a random number of times
print("\nWhatch the loop go!")
for i in range(1, random.randint(5, 15)):
    print('This for loop has already run ' + str(i) + ' times.')

# Guessing game with up to 3 attempts
print("\nLet's play a guessing game with multiple attempts (if needed)!")
attempts = 0
randomNumber = 5

while attempts < 3:
    guess = int(input("Please guess an integer between 1 and 6: "))
    if guess == randomNumber:
        print("Congrats, you got it!")
        break
    else:
        print("Oops, good luck next time!")
    attempts += 1

if guess != randomNumber:
    print(f"The correct number was {randomNumber}.")

# Loop to replace negative numbers in a list with their absolute values
print("\nLet's get the negatives out of our list!")
original = [8, 20, -10, 55, -777]
print("Original list:", original)
for i in range(len(original)):
    print(f"Index {i} value: {original[i]}")
    if original[i] < 0:
        original[i] = abs(original[i])
print("Updated list:", original)
# --------------------------------------------
# End of HOS01A Script
# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Python basics and HOS01 tutorial [Large language model]. https://openai.com/chatgpt
