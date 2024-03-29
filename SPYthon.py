#!/usr/bin/python3

##https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/
from picamera import PiCamera
from time import sleep
from datetime import datetime
import os, sys, shutil

#set up variables
cur_dir = os.getcwd()
cur_date = datetime.now()
cur_hour = cur_date.strftime('%H:%M')
image_name = '%s/spy%s.jpg' % (cur_dir,cur_hour)
camera = PiCamera()
## set up settings
camera.resolution = (2592,1944)
camera.annotate_text = "timestamp: %s" %cur_date
camera.annotate_text_size = 24

##taking the picture
print("taking a picture spy.jpg")
camera.capture(image_name)

#sending file to Pi3b

##sftp_command = """sftp slice@192.168.0.22:/home/slice/compute/SPYthon << EOF
##put %s
##chmod 777 /home/slice/compute/SPYthon/spy%s.jpg
##exit
##EOF""" % (image_name,cur_hour)
##print("transfering picture spy.jpg to rbpi3b")
#os.system(sftp_command)

# move photos to local folder
shutil.move(image_name, "~/Pictures/spy%s.jpg" % cur_hour)

print("file transfer completed")
os.system("rm %s" % image_name)


