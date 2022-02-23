import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    time.sleep(0.1)
    print(GPIO.input(PIR_PIN))

GPIO.cleanup()