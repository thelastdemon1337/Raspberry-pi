import RPi.GPIO as GPIO
import time

i = 0

def glow():
        GPIO.output(light_up, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(light_up, GPIO.LOW)
        light_up = BULBS[i + 1]
        if i > 2:
            i = 0

LED_RED_PIN = 17
LED_WHITE_PIN = 27
LED_BLUE_PIN = 22

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_WHITE_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)

GPIO.output(LED_RED_PIN, GPIO.LOW)
GPIO.output(LED_WHITE_PIN, GPIO.LOW)
GPIO.output(LED_BLUE_PIN, GPIO.LOW)

BULBS = [LED_RED_PIN,LED_WHITE_PIN,LED_BLUE_PIN]


while True:
    time.sleep(0.01)
    light_up = BULBS[i]
    prev_state = GPIO.input(BUTTON_PIN)
    if prev_state == GPIO.HIGH:
        glow()
    

# GPIO.output(LED_RED_PIN, GPIO.HIGH)
# time.sleep(2)
# GPIO.output(LED_RED_PIN, GPIO.LOW)
# GPIO.output(LED_WHITE_PIN, GPIO.HIGH)
# time.sleep(2)
# GPIO.output(LED_WHITE_PIN, GPIO.LOW)
# GPIO.output(LED_BLUE_PIN, GPIO.HIGH)
# time.sleep(2)


GPIO.cleanup()