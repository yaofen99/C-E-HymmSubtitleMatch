from PIL import Image
import pytesseract

text = ""
# image_path = "source/img.png"  # Replace with the path to your JPG image
image = Image.open("source/img.png")
text += pytesseract.image_to_string(image)
image = Image.open("source/img_1.png")
text += pytesseract.image_to_string(image)
image = Image.open("source/img_2.png")
text += pytesseract.image_to_string(image)
image = Image.open("source/img_3.png")
text += pytesseract.image_to_string(image)



print(text)

