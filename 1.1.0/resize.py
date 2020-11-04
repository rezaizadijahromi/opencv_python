import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large2.jpg')
# cv.imshow("Cat", img)

def rescal_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cap = cv.VideoCapture("Resources/Videos/dog.mp4")

while True:
    isTrue, frame = cap.read()
    frame_resized = rescal_frame(frame)
    cv.imshow("video", frame)
    cv.imshow('Video resize', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
# cv.waitKey(0)
