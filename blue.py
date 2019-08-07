import cv2
import numpy as np

cap = cv2.VideoCapture(0) #0 for first webcam and 1 for second webcam

while True:
    ret, frame = cap.read() #True or false then get frame. If no frame then false.
    blur = cv2.GaussianBlur(frame, (7,7), 0)#GaussianBlur
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)#HSV shit
########################################################################################
    #HSV shit
    LowerBlue = np.array ([30,40, 0])
    UpperBlue = np.array([150, 255, 255])
    mask = cv2.inRange(hsv, LowerBlue, UpperBlue)
########################################################################################
    #Hough Stuff
    edges = cv2.Canny(blur,100,100)#canny shit
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100)#lines
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    #HSV res needs to be down here for shits and giggles I guess
    res = cv2.bitwise_and(frame, frame, mask=mask)
########################################################################################
    cv2.rectangle(frame, (630,470), (0,200), (0,255,0),5)#creates rectangle
########################################################################################

    cv2.imshow('orignal with rectangle',frame)#showing normal frame
    cv2.imshow('Gaussian Blur', blur)#blur
    cv2.imshow('Edges', edges)#edges
    cv2.imshow('hsv', hsv)#hsv
    cv2.imshow('mask', mask)#masking
    cv2.imshow('result', res)#views result
    #How to stop the video
    if cv2.waitKey(1) & 0xFF==ord('q'): #pressing "q" on keyboard will
        break

cap.release()#release the camera
cv2.destroyAllWindows()
