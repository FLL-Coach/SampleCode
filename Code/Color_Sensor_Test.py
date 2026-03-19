from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

sensor = ColorSensor(Port.C)

while True:
    # Get the detected color
    color = sensor.color()

    # Get raw RGB values
    rgb = sensor.hsv()

    # Get reflected light intensity
    reflection = sensor.reflection()

    # Get ambient light intensity
    ambient = sensor.ambient()

    print("--- Color Sensor Readings ---")
    print("Detected Color:", color)
    print("HSV Values:", rgb)
    print("Reflection:", reflection, "%")
    print("Ambient Light:", ambient, "%")

    # React to specific colors
    if color == Color.RED:
        print("Action: RED detected - Stop!")
    elif color == Color.GREEN:
        print("Action: GREEN detected - Go!")
    elif color == Color.BLUE:
        print("Action: BLUE detected - Turn!")
    elif color == Color.YELLOW:
        print("Action: YELLOW detected - Slow down!")
    elif color == Color.WHITE:
        print("Action: WHITE detected - High reflection surface!")
    elif color == Color.BLACK:
        print("Action: BLACK detected - Low reflection surface!")
    else:
        print("Action: Unknown or no color detected.")

    print()
    wait(500)