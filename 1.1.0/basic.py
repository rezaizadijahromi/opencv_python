import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/park.jpg')
cv.imshow('Cat', img)

# Converting to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Converting to blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 150)
cv.imshow('canny', canny)

# Dilating the img
dialated = cv.dilate(canny, (5, 5), iterations=1)
cv.imshow('Dialted', dialated)

# Eroding
eroded = cv.erode(dialated, (5, 5), iterations=2)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img, (300, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('resize', resize)

# Cropping
crope = img[50:200, 200:400]
cv.imshow('crope', crope)

cv.waitKey(0)