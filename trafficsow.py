Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from gpiozero import LED
import time 

red=LED(16)
yellow=(18)
green=(17)
  
red.on()
time.sleep(5) 
red.off()
 
yellow.on()
time.sleep(2)
yellow.off()

green.on()
time.sleep(5)
green.off()