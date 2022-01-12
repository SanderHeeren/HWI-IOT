import RPi.GPIO as GPIO  # import RPi.GPIO module


led1 = 12
led2 = 13
led3 = 14
led4 = 15
input1 = 2
input2 = 3
input3 = 4
input4 = 5


GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(input1, GPIO.IN)
GPIO.setup(input2, GPIO.IN)
GPIO.setup(input3, GPIO.IN)
GPIO.setup(input4, GPIO.IN)

while True:

    if GPIO.input(input1) == GPIO.HIGH:
        GPIO.output(led1, GPIO.HIGH)
    else:
        GPIO.output(led1, GPIO.LOW)

    if GPIO.input(input2) == GPIO.HIGH:
        GPIO.output(led2, GPIO.HIGH)
    else:
        GPIO.output(led2, GPIO.LOW)

    if GPIO.input(input3) == GPIO.HIGH:
        GPIO.output(led3, GPIO.HIGH)
    else:
        GPIO.output(led3, GPIO.LOW)

    if GPIO.input(input4) == GPIO.HIGH:
        GPIO.output(led4, GPIO.HIGH)
    else:
        GPIO.output(led4, GPIO.LOW)

