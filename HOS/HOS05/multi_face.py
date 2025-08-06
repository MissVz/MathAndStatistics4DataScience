# CS506 – HOS05A: Manipulating Images
# Topic: Repeating an image (crop, resize, paste)

from PIL import Image

def multi_face():
    # resize
    img = Image.open('bulldog2.png')
    width, height = img.size
    resize = img.resize((int(width//4), int(height//4)))
    
    # flip image from left to right like mirror
    flip = resize.transpose(Image.FLIP_LEFT_RIGHT)
    fwidth, fheight = flip.size

    # add small flipped images into pattern
    pattern = Image.new('RGBA', (590, 428), 'green')
    
    # image grid 4x4
    w, h = pattern.size
    for left in range(0, w, fwidth):
        for top in range(0, h, fheight):
            pattern.paste(flip, (left, top))
    pattern.save('multi_face.png')

if __name__ == "__main__":
    multi_face()

# Reference:
# OpenAI. (2025). ChatGPT’s assistance with Pillow resizing and pasting [Large language model]. https://openai.com/chatgpt
