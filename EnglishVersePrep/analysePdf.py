import cv2

image_path = "source/page_9.jpg"
image = cv2.imread(image_path)

if image is not None:
    # Display the image
    cv2.imshow("Image", image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")


