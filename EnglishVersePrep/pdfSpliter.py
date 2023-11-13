from pdf2image import convert_from_path

# Specify the PDF file you want to convert
pdf_file = "SongsHymnsOfLife.pdf"

# Convert PDF to a list of Pillow image objects (one per page)
images = convert_from_path(pdf_file, first_page=1, last_page=10)

# Save each image as a separate file
for i, image in enumerate(images):
    image.save(f"page_{i + 1}.jpg", "JPEG")

print("PDF converted to images successfully.")
