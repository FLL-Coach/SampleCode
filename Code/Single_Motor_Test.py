from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

while True:
    motor.run_angle(500, 360)   # Forward one full rotation
    wait(500)
    motor.run_angle(500, -360)  # Backward one full rotation
    wait(500)