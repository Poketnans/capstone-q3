import base64
import os
from PIL import Image

image = Image.open("./app/assets/image_default.png")
# print("Image: ", image.)

# image.get_format_mimetype()

with open("./app/assets/image_default.png", "rb") as file:
    print("-> ", file.read())
#    converted_string = base64 .b64encode(file.read())
#    print("FILE ", converted_string)
#new_file = file.read()
# with open('encode.bin', "wb") as file:
#    file.write(converted_string)
