# CS506 – HOS05A: Manipulating Images
# Topic: Convert image file types

from PIL import Image

# Open the bulldog image and convert it to PNG
im = Image.open("bulldog.jpeg")
print("W:", im.width, "H:", im.height)

if im.format == 'JPEG':
    im.save("bulldog2.png")

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Pillow module and image format conversion [Large language model]. https://openai.com/chatgpt
