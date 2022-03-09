import base64
import os
from PIL import Image

#image = Image.open("./app/assets/image_default.png")
#print("Image: ", ima )

with open("./app/assets/image_default.png", "r", encoding='utf-8') as file:
    converted_string = base64 .b64encode(file.read())
    print("FILE ", converted_string)
    #new_file = file.read()
# with open('encode.bin', "wb") as file:
#    file.write(converted_string)
