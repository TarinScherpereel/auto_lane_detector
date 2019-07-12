import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0) #connect to webcam


#edge detection
_, im = cap.read()
cv.imshow('test',im)
edges = cv2.Canny(img,100,200) #Canny Method Algorithm

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
