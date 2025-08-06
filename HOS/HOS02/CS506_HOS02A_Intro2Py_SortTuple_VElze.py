# CS506 - HOS02 - Introduction to Python Pt 2
# Topic: Sort Tuples

def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print(sort_list_first([(5, 2), (2, 1), (4, 4), (3, 2), (1, 2)]))

# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with Python List Remove operations [Large language model]. https://openai.com/chatgpt
