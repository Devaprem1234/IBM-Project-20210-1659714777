from gpiozero import LED
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