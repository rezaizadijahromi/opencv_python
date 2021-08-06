import cv2

def empty(a):
    pass

cv2.namedWindow('Prammeters')
cv2.resizeWindow('Prammeters', 640, 240)
cv2.createTrackbar('Area', 'Prammeters', 82, 10000, empty)

cap = cv2.VideoCapture("assets/highway.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)



while True:
    success, frame = cap.read()
    height, width, _ = frame.shape

    # Get Region of intrest aka ROI
    roi = frame[340: 720,500: 800]


    mask = object_detector.apply(roi)
    # for prevent shdow detection
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areaTrack = cv2.getTrackbarPos('Area', 'Prammeters')

    for cnt in contours:

        # Clc area
        area = cv2.contourArea(cnt)
        if area > areaTrack:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)

    cv2.imshow("Roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()