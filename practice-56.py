import PIL
from PIL import Image

img = PIL.Image.open("C:\Users\User\Downloads\lokma shop photo with banner.jpg")
width, height = img.size
print(f"Width: {width}, Height: {height}")
