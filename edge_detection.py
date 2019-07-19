import cv2

capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blur image
    blurred_frame = cv2.GaussianBlur(frame, (25,25), 0)

    cv2.imshow('video gray', grayFrame)
    cv2.imshow('video blurred', blurred_frame)
    cv2.imshow('video original', frame)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
