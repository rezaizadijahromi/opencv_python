import cv2


### Read the image
# img = cv2.imread("peaky_bliners.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(2)


### Read video
# cap = cv2.VideoCapture("Vue JS Crash Course.mp4")
# cap = cv2.VideoCapture("Vue JS Crash Course.mp4")
# if not cap.isOpened():
#     print("Error opening Video File.")

# while True:
#     ret, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#     if not ret:
#         print("Can't retrieve frame - stream may have ended. Exiting..")
#         break



### Open webcam

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
### Change the brightness
# cap.set(10, 100)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('webcam', frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()


cv2.destroyAllWindows()