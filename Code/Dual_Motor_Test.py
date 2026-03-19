from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor_a = Motor(Port.A)
motor_b = Motor(Port.B)

while True:
    motor_a.run_angle(500, 360)    # Motor A forward
    motor_b.run_angle(500, 360)    # Motor B forward
    wait(500)
    motor_a.run_angle(500, -360)   # Motor A backward
    motor_b.run_angle(500, -360)   # Motor B backward
    wait(500)