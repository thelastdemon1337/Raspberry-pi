from flask import Flask
import os

FOLDER_PATH = "/home/pi/final_project_images"
log_file = FOLDER_PATH + "/photo_logs.txt"
existing_photo_counter = 0

app = Flask(__name__,static_url_path = FOLDER_PATH, static_folder = FOLDER_PATH )

@app.route("/")
def index():
    return "Hello"

@app.route("/check-movement")
def check_movement():
    response = ""
    line_counter = 0
    last_photo = ""
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            for line in f:
                line_counter += 1
                last_photo = line
                
        global existing_photo_counter
        difference = line_counter - existing_photo_counter
        existing_photo_counter = line_counter
        response = str(difference) + " new photos were taken since you last checked </br></br>"
        response += "Last Photo : " + last_photo + "</br> </br>" + "<img src = \"" + last_photo + "\">"  #<img src = "img.jpg" >
        
    
    else:
        response = "No New Photos"
        
    return response

app.run(host = "0.0.0.0")