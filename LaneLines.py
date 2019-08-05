import cv2
import numpy as np


cap = cv2.VideoCapture(0)
window = cv2.namedWindow('MainWindow',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('MainWindow',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
#isolate all blue areas of video
#turn BGR into HSV color space

_, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


#lift all blue colors from the image (blue is in 120-300 range)
#this will turn the blue white and everything else black
#specify the blue range from 60-150 (first parameters of the lower and upper bound arrays)
#use 40 -255 range for the saturation and value parameters
'''lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#detect edges in the blue mask
#use canny edge detection function (first parameter is blue mask)(second and third = lower and upper ranges for edge detection)=(200,400))
#now we should have edges for the blue areas
edges = cv2.Canny(mask, 200, 400)

def detect_edges(frame):
    # filter for blue lane lines
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("MainWindow", hsv)
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("MainWindow",mask)

    # detect edges
    edges = cv2.Canny(mask, 200, 400)

    return edges

#isolate region of region of interest we will crop top half of screen (we only care about lanes close to the vehicle)
#we will create a mask for the bottom half of the screen
#then we merge the mask with the edges to get cropped_edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # only focus bottom half of the screen
    polygon = np.array([[
        (0, height * 1 / 2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

#use hough transfrom to extract thecoordinates of these lines from these white pixels
#houghlinesP tries to fit as many lines throguh all the white pixels and return the most likely set of lines
#houghlineP detects lines using Polar coordinate
#polar coordinates include elevatin angle and distance from the original
#polar coordinates can represent both vertical lines and horizintal lines

def detect_line_segments(cropped_edges):
    # tuning min_threshold, minLineLength, maxLineGap is a trial and error process by hand
    rho = 1  # distance precision in pixel, i.e. 1 pixel
    angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
    min_threshold = 10  # minimal of votes
    line_segments = cv2.HoughLinesP(cropped_edges, rho, angle, min_threshold,
                                    np.array([]), minLineLength=8, maxLineGap=4)

    return line_segments'''

#combine 4 line segments into two lane lines
#we do this by classifying the line segments into 2 groups
#the left lane line will be upward sloping and on the left side of the screen
#the right lane line will be downward sloping and on the right side of the screen
#we take the average of the slopes and intercepts of the line segements to get the slopes and interceots of the left and right lanes
#we will use average_slope_intercept
#make_points will take a lines slope and intercept and return the endpoints of the line segement
