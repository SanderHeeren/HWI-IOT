import RPi.GPIO as GPIO  # import RPi.GPIO module
import _thread as thread
import time

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

def startThread(threadNaam, delay, state, pin):
    i = 0
    while i < delay:
        print(threadNaam + " " + str(i))
        time.sleep(delay)
        i = i + 1
        GPIO.output(pin, state)
    print("Stoppen " + threadNaam)
    if state == 1:
        thread.start_new_thread(startThread, (threadNaam, delay, 0, pin))
    else:
        thread.start_new_thread(startThread, (threadNaam, delay, 1, pin))

try:
    thread.start_new_thread(startThread, ("thread 1", 1, 1, 6))
    thread.start_new_thread(startThread, ("thread 2", 2, 1, 7))
except:
    print("error")

while 1:
    pass