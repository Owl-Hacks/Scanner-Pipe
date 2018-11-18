from scanner import scan
import cv2

cv2.namedWindow('original document', cv2.WINDOW_NORMAL)
cv2.resizeWindow('original document', 1200, 1200)

cv2.namedWindow('processed document', cv2.WINDOW_NORMAL)
cv2.resizeWindow('processed document', 1200, 1200)

cv2.namedWindow('resized document', cv2.WINDOW_NORMAL)
cv2.resizeWindow('resized document', 1200, 1200)

img = cv2.imread("./images/image0.jpg")
doc = scan(img)

height, width, channels = img.shape
print(height, width, channels)


cv2.imshow("original document", img)
cv2.imshow("processed document", doc)
cv2.imshow("resized document", doc)
cv2.waitKey(0)