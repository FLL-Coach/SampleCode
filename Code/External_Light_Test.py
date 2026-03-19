from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

light = Light(Port.C)

print("=== External Light Test ===")

# Full brightness
print("Full Brightness")
light.on(100)
wait(1000)

# Off
print("Light OFF")
light.off()
wait(1000)

# Ramp up
print("Ramping Up")
for brightness in range(0, 101, 10):
    light.on(brightness)
    print("Brightness:", brightness, "%")
    wait(300)

# Ramp down
print("Ramping Down")
for brightness in range(100, -1, -10):
    light.on(brightness)
    print("Brightness:", brightness, "%")
    wait(300)

# Blink 5 times
print("Blinking")
for i in range(5):
    light.on(100)
    wait(300)
    light.off()
    wait(300)

# Pulse effect
print("Pulse Effect")
for _ in range(3):
    for brightness in range(0, 101, 5):
        light.on(brightness)
        wait(50)
    for brightness in range(100, -1, -5):
        light.on(brightness)
        wait(50)

light.off()
print("Done!")