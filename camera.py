from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

### TAKE STILL PICTURES ###
#camera.capture("/home/pi/Desktop/test-shot.jpg")


### PREVIEW CAMERA IN 10 SEC ###
#camera.start_preview(alpha =200)
#sleep(10)
#camera.stop_preview()


### TAKE VIDEO ###
camera.start_recording("/home/pi/Desktop/video.h264")
sleep(10)
camera.stop_recording()

