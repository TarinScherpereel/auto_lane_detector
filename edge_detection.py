import cv2

capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blur image
    blurred_frame = cv2.GaussianBlur(frame, (21,21), 0)

    #canny
    #edge=cs2.Canny(frame, (25,75))
    canny = cv2.Canny(blurred_frame, 30, 100)

    cv2.imshow('video gray', grayFrame)
    cv2.imshow('video blurred', blurred_frame)
    cv2.imshow('video original', frame)
    cv2.imshow('video original', canny)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
