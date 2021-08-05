import cv2
import numpy as np
from stackImages import stackImages 


frameWidth = 640
framedHight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, framedHight)
img = cv2.imread('assets/object3.jpg')
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)

def empty(a):
    pass

cv2.namedWindow('Prammeters')
cv2.resizeWindow('Prammeters', 640, 240)
cv2.createTrackbar('Threshold1', 'Prammeters', 82, 255, empty)
cv2.createTrackbar('Threshold2', 'Prammeters', 136, 255, empty)
cv2.createTrackbar('Area', "Prammeters", 5000, 10000, empty)

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaTrack = cv2.getTrackbarPos('Area', 'Prammeters')
        if area > areaTrack:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            # True for closed contours
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)

            # Create banding box to highling where the obj
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w , y + 20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, .7, (0, 0, 255), 2)
            
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 10, y + 45), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, .7, (0, 0, 255), 2)


while True:
    # success, img = cap.read()
    imgContour = img.copy()

    threshold1 = cv2.getTrackbarPos('Threshold1', 'Prammeters')
    threshold2 = cv2.getTrackbarPos('Threshold2', 'Prammeters')


    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    # for removing noises
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    # call contour func
    getContours(imgDil, imgContour)

    imgStack = stackImages(.8, (
        [imgCanny, imgGray],[imgDil, imgContour]
        )
    )

    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
