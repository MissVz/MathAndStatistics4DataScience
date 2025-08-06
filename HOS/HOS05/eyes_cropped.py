# CS506 – HOS05A: Manipulating Images
# Topic: Cropping and duplicating part of an image

from PIL import Image

img = Image.open('bulldog2.png')

# eyes captured from this pixels
cropped = img.crop((0, 150, 590, 235))  # position of the eyes
cropped.save('eyes_cropped.png')

# paste eye cropped into the copied bulldog2.jpg
copy_img = img.copy()
copy_img.paste(cropped, (0, 0))  # paste it at position 0,0 or top left
copy_img.save('four_eyes_bulldog.png')

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Pillow cropping and positioning [Large language model]. https://openai.com/chatgpt
