import RPi.GPIO as GPIO
import time

LED_PIN16 = 16
LED_PIN15 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN15, GPIO.OUT)

while True:
    GPIO.output(LED_PIN16, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_PIN16, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(LED_PIN15, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_PIN15, GPIO.LOW)
    time.sleep(1.7)





