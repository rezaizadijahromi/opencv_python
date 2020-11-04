import cv2 as cv
import numpy as np

# img = cv.imread('resources/photos/cat.jpg')
# cv.imshow('cat', img)


blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# blank[:] = 255,0, 0
# cv.imshow('Red', blank)

## rectangle
rec = cv.rectangle(blank, (0, 0), (400, 250), (255, 0, 0), thickness=cv.FILLED)
circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=5)

# cv.imshow('Rectangle', rec)
# cv.imshow('Circle', circle)
### Text
text = cv.putText(blank, 'TRUMP',(300, 250), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), thickness=3)
cv.imshow('Text', text)

cv.waitKey(0)