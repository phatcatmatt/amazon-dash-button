import RPi.GPIO as GPIO
import time
import random

def blink(pin1, pin2):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    pin1_val = False
    pin2_val = False
    print("blinking on", pin1, pin2)

    while True:
        pin = random.randint(pin1,pin2)
        if pin == pin1:
            pin1_val = not pin1_val
            GPIO.output(pin1, GPIO.HIGH if pin1_val else GPIO.LOW)
        elif pin == pin2:
            pin2_val = not pin2_val
            GPIO.output(pin2, GPIO.HIGH if pin2_val else GPIO.LOW)
        time.sleep(random.uniform(0, .7))
