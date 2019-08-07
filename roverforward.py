# Motor1.py
# Motor forward & backward

import RPi.GPIO as GPIO
import time

Motor1 = 16
Motor2 = 20
Motor3 = 6
Motor4 = 13
EnableA = 12
EnableB = 5
#Setup
def setup():
    GPIO.setmode(GPIO.BCM)#This might be BCM instead of BOARD
    GPIO.setup(Motor1, GPIO.OUT)
    GPIO.setup(Motor2, GPIO.OUT)
    GPIO.setup(Motor3, GPIO.OUT)
    GPIO.setup(Motor4, GPIO.OUT)
    GPIO.setup(EnableA, GPIO.OUT)
    GPIO.setup(EnableB, GPIO.OUT)


def forward():
#Moving MotorA Forward
    GPIO.output(Motor1, GPIO.HIGH)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(EnableA, GPIO.LOW)

    '''GPIO.output(Motor1, GPIO.HIGH)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(EnableA, GPIO.HIGH)'''

    GPIO.output(Motor3, GPIO.HIGH)
    GPIO.output(Motor4, GPIO.LOW)
    GPIO.output(EnableB, GPIO.LOW)

    '''GPIO.output(Motor3, GPIO.HIGH)
    GPIO.output(Motor4, GPIO.LOW)
    GPIO.output(EnableB, GPIO.HIGH)'''



#Stop
'''def stop():
    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.LOW)
    GPIO.output(Motor4, GPIO.LOW)'''



print ("starting")
setup()
while True:
    print ("forward")
    forward()
    #time.sleep(2)
    #print ("stop")
    #stop()
    #time.sleep(2)
