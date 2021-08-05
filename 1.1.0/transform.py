import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Boston", img)


def translate(img, x, y):
    translateMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[0], img.shape[1])
    return cv.warpAffine(img, translateMat, dimensions)

translated = translate(img, -100, 100)

cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotate = rotate(img, 90)
cv.imshow("Rotate", rotate)


cv.waitKey(0)