import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

BUTTON_PIN5 = 5
BUTTON_PIN6 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)
gpioPins = [10, 2, 3, 4]

motor = RpiMotorLib.BYJMotor("MijnMooieMotor", "28BYJ")

try:
    while True:
        buttonState5 = GPIO.input(BUTTON_PIN5)
        buttonState6 = GPIO.input(BUTTON_PIN6)

        if buttonState5 == GPIO.HIGH:
            motor.motor_run(gpioPins, .0014, 100, True, False, "half", 0) # 5 seconden

        if buttonState6 == GPIO.HIGH:
            motor.motor_run(gpioPins, .0032, 100, False, False, "half", 0) # 12 seconden

finally:
    GPIO.cleanup()