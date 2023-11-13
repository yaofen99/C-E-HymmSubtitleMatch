from PIL import Image
import pytesseract

image_path = "source/page_9.jpg"  # Replace with the path to your JPG image
image = Image.open(image_path)

# Use pytesseract to perform OCR and extract text from the image
text = pytesseract.image_to_string(image)

print(text)
