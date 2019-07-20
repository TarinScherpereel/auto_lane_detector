import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()
    blank_frame = np.zeros_like(frame)

    #gray video
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blur video
    blurred_frame = cv2.GaussianBlur(grayFrame, (21,21), 0)

    #canny
    edge=cs2.Canny(frame, (25,75))

    #canny method
    canny = cv2.Canny(blurred_frame, 30, 100)

    #select edges for hough transform
    #edges = cv2.Canny(canny, 50, 200)

    #select lines through Hough Transform
    #lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100)

    #Part of hough transform
    #try:
        #for line in lines:
            #x1, y1, x2, y2 = line[0]
            #cv2.line(blank_frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
    #except TypeError:
        #print('Found no lines')
    #cv2.imshow('video gray', grayFrame)
    #cv2.imshow('video blurred', blurred_frame)
    #window = cv2.namedWindow('MainWindow',cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty('MainWindow',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('video canny', canny)
    cv2.imshow('video original', frame)
    #new
    #cv2.imshow("MainWindow", blank_frame)
    # cv2.imshow('final')


    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
