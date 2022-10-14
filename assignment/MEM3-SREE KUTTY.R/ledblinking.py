import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
   GPIO.output(8,True)
   print("led is on")
   time.sleep(1)
   GPIO.output(8,False)
   print("led is off") 
   time.sleep(1)
