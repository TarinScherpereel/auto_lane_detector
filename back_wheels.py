# Motor1.py
# Motor forward & backward

import RPi.GPIO as GPIO
from time import sleep

P_MOTA1 = 16
P_MOTA2 = 20
P_MOTA3 = 6
P_MOTA4 = 13

def forward():
    #Moving forward motor a
    GPIO.output(P_MOTA3, GPIO.LOW)
    GPIO.output(P_MOTA4, GPIO.HIGH)
    GPIO.output(P_MOTA4, GPIO.HIGH)
    GPIO.output(P_MOTA3, GPIO.LOW)
    #moving forward motor b
    GPIO.output(P_MOTA3, GPIO.HIGH)
    GPIO.output(P_MOTA4, GPIO.LOW)
    GPIO.output(P_MOTA4, GPIO.LOW)
    GPIO.output(P_MOTA3, GPIO.HIGH)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(P_MOTA1, GPIO.OUT)
    GPIO.setup(P_MOTA2, GPIO.OUT)
    GPIO.setup(P_MOTA3, GPIO.OUT)
    GPIO.setup(P_MOTA4, GPIO.OUT)

print ("starting")
setup()
while True:
    print ("forward")
    forward() 