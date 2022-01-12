import RPi.GPIO as GPIO  # import RPi.GPIO module
import time


led6 = 6
led7 = 7
input3 = 21
input2 = 5
KNOP = 4
State3 = GPIO.LOW
State2 = GPIO.LOW

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)
GPIO.setup(input2, GPIO.IN)
GPIO.setup(input3, GPIO.IN)
GPIO.setup(KNOP, GPIO.IN, GPIO.PUD_DOWN)

while True:
    buttonState = GPIO.input(KNOP)
    State2 = GPIO.input(input2)
    State3 = GPIO.input(input3)
    print("State 2 " + str(State2))
    print("State 3 " + str(State3))

    if buttonState == GPIO.HIGH:
        GPIO.output(led6, GPIO.LOW)
        GPIO.output(led7, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led6, GPIO.HIGH)
        GPIO.output(led7, GPIO.LOW)
        time.sleep(1)
    else:
        if State2 == GPIO.HIGH:
            GPIO.output(led6, GPIO.HIGH)
        else:
            GPIO.output(led6, GPIO.LOW)
        if State3 == GPIO.HIGH:
            GPIO.output(led7, GPIO.HIGH)
        else:
            GPIO.output(led7, GPIO.LOW)
