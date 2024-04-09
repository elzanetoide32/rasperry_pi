import time
import RPi.GPIO as GPIO
pin=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

#GPIO.output(pin,GPIO.HIGH)
#GPIO.output(pin,GPIO.LOW)

for i in range(0, 30):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()