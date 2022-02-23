from picamera import PiCamera
import time

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1280,720)
time.sleep(2)

file_name = "/home/pi/camera/py_image.jpg"

camera.capture(file_name)
print("Image captured")