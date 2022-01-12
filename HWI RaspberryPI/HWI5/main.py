import RPi.GPIO as GPIO
import time


def millis():
    return time.time() * 1000


LED_PIN16 = 16
LED_PIN15 = 15
BUTTON_PIN5 = 5
BUTTON_PIN7 = 7
previousMillis1 = 0
previousMillis2 = 0
LED_STATE15 = GPIO.LOW
LED_STATE16 = GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN15, GPIO.OUT)
GPIO.setup(BUTTON_PIN5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN7, GPIO.IN, GPIO.PUD_DOWN)

while True:
    buttonState5 = GPIO.input(BUTTON_PIN5)
    buttonState7 = GPIO.input(BUTTON_PIN7)
    currentMillis = millis();

    if currentMillis - previousMillis1 > 1000 and buttonState5 == GPIO.HIGH:
        previousMillis1 = currentMillis
        if LED_STATE15 == GPIO.HIGH:
            GPIO.output(LED_PIN15, GPIO.LOW)
            LED_STATE15 = GPIO.LOW
        else:
            GPIO.output(LED_PIN15, GPIO.HIGH)
            LED_STATE15 = GPIO.HIGH
    if LED_STATE15 == GPIO.HIGH:
        if currentMillis - previousMillis1 > 1300 and buttonState5 == GPIO.LOW:
            previousMillis1 = currentMillis
            GPIO.output(LED_PIN15, GPIO.LOW)
            LED_STATE15 = GPIO.LOW

    if LED_STATE15 == GPIO.LOW:
        if currentMillis - previousMillis1 > 700 and buttonState5 == GPIO.LOW:
            previousMillis1 = currentMillis
            GPIO.output(LED_PIN15, GPIO.HIGH)
            LED_STATE15 = GPIO.HIGH

    if buttonState7 == GPIO.HIGH:
        if currentMillis - previousMillis2 > 700:
            previousMillis2 = currentMillis
            if LED_STATE16 == GPIO.HIGH:
                GPIO.output(LED_PIN16, GPIO.LOW)
                LED_STATE16 = GPIO.LOW
            else:
                GPIO.output(LED_PIN16, GPIO.HIGH)
                LED_STATE16 = GPIO.HIGH
    else:
        GPIO.output(LED_PIN16, GPIO.LOW)
        LED_STATE16 = GPIO.LOW

