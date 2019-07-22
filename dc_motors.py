# Motor1.py
# Motor forward & backward

import RPi.GPIO as GPIO
from time import sleep

P_MOTA1 = 16
P_MOTA2 = 20
P_MOTA3 = 6
P_MOTA4 = 13

def forward():
    GPIO.output(P_MOTA1, GPIO.HIGH)
    GPIO.output(P_MOTA2, GPIO.LOW)
    GPIO.output(P_MOTA3, GPIO.LOW)
    GPIO.output(P_MOTA4, GPIO.HIGH)

def backward():
    GPIO.output(P_MOTA1, GPIO.LOW)
    GPIO.output(P_MOTA2, GPIO.HIGH)


def stop():
    GPIO.output(P_MOTA1, GPIO.LOW)
    GPIO.output(P_MOTA2, GPIO.LOW)
    GPIO.output(P_MOTA3, GPIO.LOW)
    GPIO.output(P_MOTA4, GPIO.LOW)

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
    print ("backward")
    backward()
    time.sleep(2)
    print ("stop")
    stop()
    time.sleep(2)
