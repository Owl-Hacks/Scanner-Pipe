import cv2
import numpy as np


def cancel_noise(img):
    # blur and make image binary
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.bilateralFilter(img, 9, 75, 75)
    # img = cv2.medianBlur(img, 5)

    upper = np.array([255])
    lower = np.array([120])

    mask = cv2.inRange(img, lower, upper)

    return mask


def resize(img):
    # resize to proportionally to 1120x800, if it doesn't fill, fill it with white space
    height, width = img.shape
    print(height, width)

    # ratio = list(map(int, str(Fraction(height, width)).split("/")))
    ratio = width/height
    n_height = round(800/ratio)
    n_width = round(1120*ratio)

    print(n_height, n_width)
    return img