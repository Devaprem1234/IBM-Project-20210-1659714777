Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO 
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

