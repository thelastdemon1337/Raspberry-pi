import yagmail

password = ""

with open("/home/pi/.local/share/.gmail_password", "r") as f:
    password = f.read()
    
yag = yagmail.SMTP('tarun.raspberrypi@gmail.com', password)

yag.send(to = 'tarunkotagiri3007@gmail.com',
         subject = "Raspberry pi 4 official guide",
         contents = "From Raspbian.. Make good use of it if needed.",
         attachments = "/home/pi/Bookshelf/000_RPi_BeginnersGuide_DIGITAL.pdf")


print("Email sent")