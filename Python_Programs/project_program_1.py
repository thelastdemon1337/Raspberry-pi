import RPi.GPIO as GPIO
import time, os
from picamera import PiCamera
import yagmail


print("Starting up 'set up' protocols")

#Camera setup
camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
print("Waiting 2 seconds to init Camera")
time.sleep(2)
print("Camera setup Okay")

#yagmail setup
password = ""

with open("/home/pi/.local/share/.gmail_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP('tarun.raspberrypi@gmail.com', password)

print("Email sender setup okay")

#FOLDER TO STORE CAMERA IMAGES
FOLDER_NAME = "/home/pi/final_project_images"
file_name = "/img_"
log_file = "/home/pi/final_project_images/photo_logs.txt"

LED_PIN = 27
PIR_PIN = 4

MOV_DTECT_THRESHOLD = 3.0
MIN_DURATION_BETWEEN_2_PHOTOS = 60.0


# GPIOs Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print("GPIOs Setup Okay.")
print("Everything has been successfully set up!")

last_pir_state = GPIO.input(PIR_PIN)
movement_time = time.time()
last_photo_taken = 0

def log(name_of_the_photo):
    with open(log_file , "a") as f:
        f.write(name_of_the_photo + "\n")
        
def send_email_with_photo(dest):
    yag.send(to = 'tarunkotagiri3007@gmail.com',
             subject = "Movement Detected!",
             contents = "Detected a continuous movement for 3 seconds.. Here's what it was..",
             attachments = dest)
    print("Email sent! check 'tarun********3007@gmail.com' for more details.")

def shoot():
    dest = FOLDER_NAME + file_name + str(time.time()) + ".jpg"
    camera.capture(dest)
    log(dest)
    send_email_with_photo(dest)
    


def take_photo():
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)    
    shoot()
    

    
    

try:
    if os.path.exists(log_file):
        os.remove(log_file)
    while True:
        time.sleep(0.1)
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        pir_state = GPIO.input(PIR_PIN)
        if last_pir_state == GPIO.LOW and pir_state == GPIO.HIGH:
            movement_time = time.time()
        if last_pir_state == GPIO.HIGH and pir_state == GPIO.HIGH:
            if time.time() - movement_time > MOV_DTECT_THRESHOLD:
                if time.time() - last_photo_taken > MIN_DURATION_BETWEEN_2_PHOTOS:
                    print("Movement Detected! Collecting Evidence..")
                    #code to take a picture and send it through email
                    
                    take_photo()
                    last_photo_taken = time.time()
                   
        last_pir_state = pir_state
        
except KeyboardInterrupt:
    GPIO.cleanup()
    

