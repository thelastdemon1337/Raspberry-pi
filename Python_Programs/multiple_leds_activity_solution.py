import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
LED_2_PIN = 27
LED_3_PIN = 22
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
GPIO.setup(LED_3_PIN, GPIO.OUT)

GPIO.output(LED_1_PIN, GPIO.LOW)
GPIO.output(LED_2_PIN, GPIO.LOW)
GPIO.output(LED_3_PIN, GPIO.LOW)

prev_button_state = GPIO.input(BUTTON_PIN)

led_index = 0

while True:
    time.sleep(0.01)
    current_button_state = GPIO.input(BUTTON_PIN) 
    if prev_button_state != current_button_state:
        prev_button_state = current_button_state
        if current_button_state == GPIO.HIGH:
            if led_index == 0:
                #on led 1
                GPIO.output(LED_1_PIN, GPIO.HIGH)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.LOW)
                led_index = 1
            elif led_index == 1:
                #on led
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.HIGH)
                GPIO.output(LED_3_PIN, GPIO.LOW)
                led_index = 2
            else:
                #on led
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.HIGH)
                led_index = 0
            
        
    
        
GPIO.cleanup()