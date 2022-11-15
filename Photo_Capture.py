from picamera import PiCamera
import time 

camera = PiCamera()

camera.start_preview()

time.sleep(1)

camera.capture('/home/doc/image.png')
camera.stop
