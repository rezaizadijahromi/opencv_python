import cv2
import numpy as np

## Read the image
img = cv2.imread("peaky_bliners.jpg")
cv2.imshow("Output", img)
cv2.waitKey(2)


## Read video
cap = cv2.VideoCapture("Vue JS Crash Course.mp4")
cap = cv2.VideoCapture("Vue JS Crash Course.mp4")
if not cap.isOpened():
    print("Error opening Video File.")

while True:
    ret, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if not ret:
        print("Can't retrieve frame - stream may have ended. Exiting..")
        break



## Open webcam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
## Change the brightness
cap.set(10, 100)

while True:
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()

 
cv2.destroyAllWindows()


## Make image blur or gray and find edges

img = cv2.imread("peaky_bliners.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDialation)
cv2.imshow("Erodetion", imgEroded)


cv2.waitKey(100000)

## Resizing and crop

img = cv2.imread("peaky_bliners.jpg")
print(img.shape)

imgResize = cv2.resize(img, (150, 200))
imgCropp = img[]

cv2.imshow('Image', img)
cv2.imshow('Resize', imgResize)

cv2.waitKey(100000)

cv2.destroyAllWindows()


