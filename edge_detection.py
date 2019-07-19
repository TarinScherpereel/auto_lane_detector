import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blur image
    blurred_frame = cv2.GaussianBlur(grayFrame, (21,21), 0)

    #canny
    #edge=cs2.Canny(frame, (25,75))
    canny = cv2.Canny(blurred_frame, 30, 100)

    #new
    edges = cv2.Canny(canny, 50, 200)

    #new
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200)

    #new
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

    #cv2.imshow('video gray', grayFrame)
    #cv2.imshow('video blurred', blurred_frame)
    cv2.imshow('video canny', canny)
    cv2.imshow('video original', frame)
    #new
    cv2.imshow("Result Image", frame)
    # cv2.imshow('final')


    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
