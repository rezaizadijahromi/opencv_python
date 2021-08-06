import cv2

cap = cv2.VideoCapture("assets/highway.mp4")

object_detector = cv2.createBackgroundSubtractorKNN()

while True:
    success, frame = cap.read()

    mask = object_detector.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    