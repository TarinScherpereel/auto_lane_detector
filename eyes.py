import cv2
import numpy as np

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)

    while(camera.isOpened()):
        _, image = camera.read()
        cv2.imshow("original", image)

        b_w_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Black/White', b_w_image)

        if cv2.waitKey(1) &0xFF == ord('q') :
            break

        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
