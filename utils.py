import cv2
import numpy as np


def cancel_noise(img):
    # blur and make image binary
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.bilateralFilter(img, 9, 75, 75)
    img = cv2.medianBlur(img, 5)

    upper = np.array([255])
    lower = np.array([160])

    mask = cv2.inRange(img, lower, upper)

    return mask

def resize(img):
    return img