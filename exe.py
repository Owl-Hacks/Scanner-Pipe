from scanner import scan
from utils import *
from takePicture import *
import cv2

video_capture()

cv2.namedWindow('original document', cv2.WINDOW_NORMAL)
cv2.resizeWindow('original document', 1200, 1200)

cv2.namedWindow('processed document', cv2.WINDOW_NORMAL)
cv2.resizeWindow('processed document', 1200, 1200)

# cv2.namedWindow('resized document', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('resized document', 1200, 1200)

img = cv2.imread("./images/image0.jpg")
doc = scan(img)


# res = resize(doc)

cv2.imshow("original document", img)
kernel = np.ones((3, 3), np.uint8)

doc = cv2.erode(doc, kernel, iterations=1)
doc = cv2.dilate(doc, kernel, iterations=1)
cv2.imshow("processed document", doc)

cv2.imwrite("./processed/processed3.jpg", doc)


cv2.waitKey(0)