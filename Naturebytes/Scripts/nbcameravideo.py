#!/usr/bin/python
# Naturebytes Wildlife Cam Kit | V1.07 (Pixel)
# Based on the excellent official Raspberry Pi tutorials and a little extra from Naturebytes

import RPi.GPIO as GPIO
import time
from subprocess import call
from datetime import datetime
import logging

# Logging all of the camera's activity to the "naturebytes_camera_log" file. If you want to watch what your camera
# is doing step by step you can open a Terminal window and type "cd /Naturebytes/Scripts" and then type
# "tail -f naturebytes_camera_log" - leave this Terminal window open and you can view the logs live 

logging.basicConfig(format='%(asctime)s %(message)s',filename='naturebytes_camera_log',level=logging.DEBUG)
logging.info('Naturebytes Wildlife Cam Kit started up successfully')

# Assigning a variable to the pins that we have connected the PIR to
sensorPin = 13

# *** Legacy Kickstarter edition only *** You may want to detect the battery status (low or high) if using a Powerboost, so we code commented out a way of doing this to assist using pin 15
# lowbattPin = 15

# Setting the GPIO (General Purpose Input Output) pins up so we can detect if they are HIGH or LOW (on or off)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(lowbattPin, GPIO.IN)

# Defining our default states so we can detect a change

prevState = False
currState = False
# prevBattState = False
# currBattState = False

# Starting a loop

while True:
    time.sleep(0.1)
    prevState = currState
    # prevBattState = currBattState
    
    # Map the state of the camera to our input pins (jumper cables connected to your PIR)

    currState = GPIO.input(sensorPin)
    # currBattState = GPIO.input(lowbattPin)

    # Checking that our state has changed
   
    if currState != prevState:
    # About to check if our new state is HIGH or LOW

        newState = "HIGH" if currState else "LOW"
        #  newBattState = "HIGH" if currBattState else "LOW"        
        print "GPIO pin %s is %s" % (sensorPin, newState)
        # print "Battery level detected via pin %s is %s" % (lowbattPin, newBattState)

        if currState:  # Our state has changed, so that must be a trigger from the PIR       
     
            i = datetime.now() # Get the time now
            get_date = i.strftime('%Y-%m-%d') # Get and format the date
            get_time = i.strftime('%H-%M-%S.%f') # Get and format the time
            # batt_state = newBattState
            # Checking the current status of the battery

            # Recording that a PIR trigger was detected and logging the battery level at this time
            logging.info('PIR trigger detected')
            # logging.info('Battery level is %(get_batt_level)s', { 'get_batt_level': batt_state })

            # Assigning a variable so we can create a video mp4 (h264) file that contains the date and time as its name
            video = get_date + '_' +  get_time + '.h264'

            # Using the raspivid library to take a video. You can show that a video has been taken in a small preview box on the desktop by changing --nopreview to --preview
            cmd = 'raspivid -t 15000 -w 1280 -h 720 --nopreview -o /media/usb0/' + video
	    print 'cmd ' +cmd

            # If you find you have permission problems saving to other attached non-Naturebytes storage devices you can use this line to change the owner of the video if required
            # perms = 'chown pi:pi /media/usb0/' + video
            # print 'perms ' +perms            

            # Log that we have just taking a video"
            logging.info('About to take a video and save to the USB drive')
            call ([cmd], shell=True)
            # call ([perms], shell=True)
            
            # Log that a video was taken successfully and state the file name so we know which one"
            logging.info('Video taken successfully %(show_video_name)s', { 'show_video_name': video })
            video_location =  '/media/usb0/' + video

            # Log that we are about to attempt to write the overlay text. This was removed in v1.07 to speed up the capture process."
            logging.info('Skipping legacy overlay text')            

            # overlay = "/usr/bin/convert "+ video_location + " "

            # Use ImageMagick to write text and meta data onto the video.
            # overlay += " -gravity north -background black -extent +0+40 +repage -box black -fill white -pointsize 24 -gravity southwest -annotate +6+6 'Naturebytes Wildlife Cam Kit | Date & Time: " + get_date + '" '" + get_time '" -gravity southeast -annotate +6+6 'Camera 1 " "'" + photo_location
            # overlay += " -gravity north -background black -extent +0+40 +repage -box black -fill white -pointsize 24 -gravity southwest -annotate +6+6 'Naturebytes Wildlife Cam Kit | Date & Time: " + get_date + " " + get_time + "' -gravity southeast -annotate +6+6 'Camera 1' " + photo_location   
            
            # Log that we the text was added successfully"
            # logging.info('Added the overlay text successfully')
            # call ([overlay], shell=True)

            # Add a small Naturebytes logo to the top left of the video. Note - you could change this to your own logo if you wanted.
            # logging.info('Adding the Naturebytes logo')
            # overlay = '/usr/bin/convert '+ video_location + ' /home/pi/Naturebytes/Scripts/naturebytes_logo_80.png -geometry +1+1 -composite ' + video_location
            # call ([overlay], shell=True)

            # Log that the logo was added succesfully"
            # logging.info('Logo added successfully')            

        else:

           # print "Waiting for a new PIR trigger to continue"
           logging.info('Waiting for a new PIR trigger to continue')

# END
