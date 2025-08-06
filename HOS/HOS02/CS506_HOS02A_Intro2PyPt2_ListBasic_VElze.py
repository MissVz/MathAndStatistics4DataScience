# CS506 - HOS02 - Introduction to Python Pt 2
# Topic: Basic List Operations

# List_basic.py
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# access
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# update
print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2001
print("New value available at index 2 : ")
print(list1[2])

# add
list1.append(2020)
print("New List:", list1)

# insert
list1.insert(0, 'Python')
print("After inserting: ", list1)


# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with Python List operations [Large language model]. https://openai.com/chatgpt
