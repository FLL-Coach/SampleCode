from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

sensor = UltrasonicSensor(Port.C)

while True:
    distance = sensor.distance()
    print("Distance:", distance, "mm")

    if distance < 150:
        print("Object nearby! Less than 150mm away.")
    else:
        print("Path is clear.")

    wait(500)