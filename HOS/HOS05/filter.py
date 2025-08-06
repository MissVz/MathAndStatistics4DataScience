# CS506 – HOS05A: Manipulating Images
# Topic: Filtering images

from PIL import Image, ImageFilter

# Open and apply blur
im = Image.open("bulldog2.png")
blurred = im.filter(ImageFilter.BLUR)
blurred.save("blur.jpg")

# Convert to grayscale
gray = im.convert("L")
gray.save("grayscale.png")

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Pillow filtering and grayscale conversion [Large language model]. https://openai.com/chatgpt
