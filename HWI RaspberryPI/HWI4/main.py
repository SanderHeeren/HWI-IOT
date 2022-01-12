import RPi.GPIO as GPIO
import time


LED_PIN16 = 16
LED_PIN15 = 15
BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN15, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

while True:
    buttonState = GPIO.input(BUTTON_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN15, GPIO.LOW)
        GPIO.output(LED_PIN16, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN16, GPIO.LOW)
        time.sleep(0.7)
    else:
        GPIO.output(LED_PIN15, GPIO.HIGH)
