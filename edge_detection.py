import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0) #connect to webcam


#edge detection
_, im = cap.read()
cv2.imshow('test',im)
cv2.waitKey(0)
edges = cv2.Canny(img,100,200) #Canny Method Algorithm

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
#
