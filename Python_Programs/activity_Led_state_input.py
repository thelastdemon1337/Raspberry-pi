import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

state = int(input("Enter 1 to light up the LED And 0 to power Off"))

if state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)
elif state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
    
    
time.sleep(2)
GPIO.cleanup()