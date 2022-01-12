import RPi.GPIO as GPIO
import time

servoPin = 17
BUTTON_PIN5 = 5
BUTTON_PIN6 = 6

# initialize GPIO Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.output(servoPin, GPIO.LOW)
GPIO.setup(BUTTON_PIN5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)

# initialize PWM in defined GPIO Pin
global p
p = GPIO.PWM(servoPin, 50)
p.start(2.5)


# rotate the servo to a specific angle
def servoWrite(angle, stop):
    #dutycycle = ((angle / 180.0) + 1.0) * 5.0

    for i in range(0, angle+1, 10):
        p.ChangeDutyCycle(2.5 + stop * i / angle)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.02)

    time.sleep(stop/10)

    for i in range(angle+1, 0, -10):
        p.ChangeDutyCycle(2.5 + stop * i / angle)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.02)


try:
    while True:
        buttonState5 = GPIO.input(BUTTON_PIN5)
        buttonState6 = GPIO.input(BUTTON_PIN6)

        if buttonState5 == GPIO.HIGH:
            servoWrite(120, 10)

        if buttonState6 == GPIO.HIGH:
            servoWrite(120, 5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

