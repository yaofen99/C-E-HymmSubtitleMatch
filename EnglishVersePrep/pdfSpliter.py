from pdf2image import convert_from_path

pdf_file = "./source/SongsHymnsOfLife.pdf"

images = convert_from_path(pdf_file, first_page=1, last_page=15)

for i, image in enumerate(images):
    image.save(f"source/page_{i + 1}.jpg", "JPEG")
    # after several trial, prefer not to resize img

print("PDF converted to images successfully.")
