import random
temp_sensor_value=random.randint(12,59)
humidity_value=random.randint(82,268)
if temp_sensor_value>30 or humidity_value>90:
    print("Temperature value:",temp_sensor_value)
    print("Humidity value:",humidity_value)
    print("Hazard detected")
