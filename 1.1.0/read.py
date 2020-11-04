import cv2 as cv
import os

cap = cv.VideoCapture("Resources/Videos/dog.mp4")

while True:
    isTrue, frame = cap.read()

    cv.imshow("video", frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break


cv.waitkey(10000)