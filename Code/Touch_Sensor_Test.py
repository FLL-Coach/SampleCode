from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

touch = ForceSensor(Port.C)

while True:
    if touch.pressed():
        print("Sensor is pressed! Force:", touch.force(), "N")
    else:
        print("Sensor is not pressed.")

    wait(200)