# CS506 – HOS05A: Manipulating Images
# Topic: Image Colors

from PIL import ImageColor

# Get RGBA color value of white
print("RGBA for 'white':", ImageColor.getcolor('white', 'RGBA'))
print("RGBA for 'blue':", ImageColor.getcolor('blue', 'RGBA'))
print("RGBA for 'dark blue':", ImageColor.getcolor('darkblue', 'RGBA'))
print("RGBA for 'chocolate':", ImageColor.getcolor('chocolate', 'RGBA'))


# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Pillow module and RGBA values [Large language model]. https://openai.com/chatgpt