from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Mecanum wheels - all 4 corners
front_left  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.B)
rear_left   = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rear_right  = Motor(Port.D)

def mecanum_drive(forward, strafe, rotate, speed=500):
    """
    forward: positive = forward, negative = backward
    strafe:  positive = right,   negative = left
    rotate:  positive = clockwise, negative = counterclockwise
    """
    fl = forward + strafe + rotate
    fr = forward - strafe - rotate
    rl = forward - strafe + rotate
    rr = forward + strafe - rotate

    # Scale to max speed
    max_val = max(abs(fl), abs(fr), abs(rl), abs(rr), 1)
    scale = speed / max_val

    front_left.run(fl * scale)
    front_right.run(fr * scale)
    rear_left.run(rl * scale)
    rear_right.run(rr * scale)

# Drive forward
mecanum_drive(1, 0, 0)
wait(1000)

# Strafe right
mecanum_drive(0, 1, 0)
wait(1000)

# Strafe left
mecanum_drive(0, -1, 0)
wait(1000)

# Rotate clockwise
mecanum_drive(0, 0, 1)
wait(1000)

# Stop
front_left.stop()
front_right.stop()
rear_left.stop()
rear_right.stop()