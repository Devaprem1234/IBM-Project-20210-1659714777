Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
temp_sensor_value=random.randint(56,22)
humidity_value=random.randint(34,87)
if temp_sensor_value>30 or humidity_value>90:
    print("Temperature value:",temp_sensor_value)
    print("Humidity value:",humidity_value)
    print("Hazard detected")
