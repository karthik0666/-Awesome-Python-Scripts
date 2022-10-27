from PIL import Image
#Capture the path where your image is stored
image_1 = Image.open(r'path where the image is stored\file name.png')
#Convert the image to PDF using Python
im_1 = image_1.convert('RGB')
#PDF file will be stored under the same path where the original image is stored
im_1.save(r'path where the pdf will be stored\new file name.pdf')