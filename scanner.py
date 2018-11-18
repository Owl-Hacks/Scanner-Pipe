from transform import four_point_transform
from utils import *
from skimage.filters import threshold_local
import cv2
import imutils


def scan(img):
    ratio = img.shape[0] / 500.0

    # save original so it doesnt get changed
    orig = img.copy()
    image = imutils.resize(img, height=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cancel_noise(gray)

    binary = cv2.Canny(gray, 75, 200)

    try:
        im2, cnts, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = max(cnts, key=cv2.contourArea)

        # approximate the contour
        peri = cv2.arcLength(cnts, True)

        approx = cv2.approxPolyDP(cnts, 0.02 * peri, True)
        assert len(approx) == 4

        cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)

        # apply the four point transform to obtain a top-down
        # view of the original image
        warped = four_point_transform(orig, approx.reshape(4, 2) * ratio)

        # convert the warped image to grayscale, then threshold it
        # to give it that 'black and white' paper effect
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = threshold_local(warped, 11, offset=10, method="gaussian")
        warped = (warped > T).astype("uint8") * 255

        return warped

    except:
        print("Unacceptable photo, try taking another one!")