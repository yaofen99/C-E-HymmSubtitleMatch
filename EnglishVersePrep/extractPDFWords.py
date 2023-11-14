import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

# assume an input list
# always start from 0 and ends with 1100
# spacing = [520, 770, 900]
paragraphNum = 4

# Step1: Read image, to grayscale, edge detection
# Read image
image = cv2.imread('source/page_14.jpg')
image = cv2.resize(image, (1200, 1800))

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Step2: HoughLinesP, save line in lines

lines = cv2.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=200,  # Min number of votes for valid line
    minLineLength=100,  # Min allowed length of line
    maxLineGap=3  # Max allowed gap between line for joining them
)

# if lines is not None:
#     for i in range(0, len(lines)):
#         l = lines[i][0]
#         cv2.line(image, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

# plt.imshow(image)
# plt.show()

# Step3: Extract line from lines

leftParaphraseLine = set()
for point in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = point[0]
    # x is about 105
    if x1 < 90 or x1 > 115 or x2 < 90 or x2 > 115 or abs(y1 - y2) < 10:
        continue
    #     print(x1)
    newLine = True
    if len(leftParaphraseLine) == 0:
        leftParaphraseLine.add((y1, y2))
    else:
        # check if it can merge
        for p in leftParaphraseLine:
            # same line detected
            # case1: former line in new line
            if (p[0] > y2 - 10 and p[0] < y1 + 10) or (p[1] > y2 - 10 and p[1] < y1 + 10) \
                    or (y1 < p[0] + 10 and y1 > p[1] - 10) or (y2 < p[0] + 10 and y2 > p[1] - 10):
                p = (max(y1, p[0]), min(y2, p[1]))
                newLine = False
        if newLine:
            leftParaphraseLine.add((y1, y2))

leftParaphraseLine = sorted(leftParaphraseLine)
# print(leftParaphraseLine)
# for point in points:
#     cv2.line(image,(105,point[1]),(105,point[0]),(0,255,0),2)
# plt.imshow(image)
# plt.show()


# Step4: Fragment image
# Step4: Extract text

# crop example(not finish yet)
xStart = 180
xWinLen = 900
yUpMargin = 75
yLowMargin = 85
crop = 0

textArr = [""] * paragraphNum

cnt = 0

stop = 0
for line in leftParaphraseLine:
    #     if(stop==1):
    #         continue
    #     stop=1
    #     for i in range(paragraphNum):
    #         start = 0
    #         end = 0
    #         if(i==0):
    #             start=0
    #             end=spacing[0]
    #         elif(i== paragraphNum-1):
    #             start=spacing[i]
    #             end=1100
    #         else:
    #             start=spacing[i-1]
    #             end=spacing[i]

    # crop img
    crop = image[line[1] + yUpMargin:line[0] - yLowMargin, xStart:xStart + xWinLen]

    rawData = pytesseract.image_to_string(crop)
    lines = rawData.split("\n")

    for SingleLine in lines:
        if len(SingleLine) < 5:
            continue
        # print(cnt)
        textArr[cnt] += SingleLine
        cnt = cnt + 1
        cnt = cnt % paragraphNum

    # plt.imshow(crop)
    # plt.show()
    # print()

for par in textArr:
    print(par)
    print("\n\n")

