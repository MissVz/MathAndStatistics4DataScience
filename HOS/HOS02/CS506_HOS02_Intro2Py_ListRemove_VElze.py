# CS506 - HOS02 - Introduction to Python Pt 2
# Topic: List Remove

#del
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)
print("\n")

#pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a", first_owned)
print("\n")

#remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
print("\n")

original = [8, 20, -10, 55, -777]

# using loops in lists
for i in range(len(original)):
    print(original[i])

# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with Python List Remove operations [Large language model]. https://openai.com/chatgpt
