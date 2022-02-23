from picamera import PiCamera
import time, os

FOLDER_NAME = "/home/pi/camera_series_activity"

camera = PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
time.sleep(2)

def shoot():
    file_name = FOLDER_NAME + "/ser_img"
    for i in range(1,11):
        camera.capture(file_name + str(i) + ".jpg")
        print("Image" + str(i) + " Captured")
        time.sleep(5)

if os.path.exists(FOLDER_NAME):
    print("Directory Exists")
    shoot()
    
else:
    os.mkdir(FOLDER_NAME)
    print("New Directory created")
    shoot()
    
    
    