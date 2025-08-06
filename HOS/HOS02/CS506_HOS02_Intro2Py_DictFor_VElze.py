# CS506 - HOS02 - Introduction to Python Pt 2
# Topic: Looping in Dictionary

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}

aliens = [alien_0, alien_1]

#Accessing key,value
for i in aliens:
    for key, value in i.items():
        print("KEY: ", key, "\t", "VALUE :", value)


# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with Python List Remove operations [Large language model]. https://openai.com/chatgpt
