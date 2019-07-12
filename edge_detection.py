import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0) #connect to webcam

#edge detection

img = cv2.imread('VideoCapture',0)
edges = cv2.Canny(img,100,200) #Canny Method Algorithm

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
