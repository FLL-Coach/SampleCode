from pybricks.pupdevices import ColorLightMatrix
from pybricks.parameters import Port, Color
from pybricks.tools import wait

light_matrix = ColorLightMatrix(Port.C)

print("=== Color Light Matrix Test ===")

# --- Test 1: Single color, all 9 lights ---
print("Color Test")
for color in [Color.RED, Color.GREEN, Color.BLUE,
              Color.YELLOW, Color.CYAN, Color.MAGENTA, Color.WHITE]:
    light_matrix.on(color)
    print("Color:", color)
    wait(700)

# --- Test 2: Off ---
print("Lights OFF")
light_matrix.off()
wait(1000)

# --- Test 3: Each light a different color using a list of 9 ---
print("Multi Color Test")
light_matrix.on([
    Color.RED,     Color.GREEN,   Color.BLUE,
    Color.YELLOW,  Color.CYAN,    Color.MAGENTA,
    Color.WHITE,   Color.RED,     Color.GREEN
])
wait(2000)

# --- Test 4: Repeating pattern using list multiplication ---
print("Pattern Test")
light_matrix.on([Color.RED, Color.WHITE, Color.BLUE] * 3)
wait(2000)

# --- Test 5: Brightness fade using Color scaling ---
print("Fade Effect")
for _ in range(3):
    for brightness in range(0, 110, 10):
        light_matrix.on(Color.BLUE * (brightness / 100))
        wait(50)
    for brightness in range(100, -10, -10):
        light_matrix.on(Color.BLUE * (brightness / 100))
        wait(50)

light_matrix.off()
print("Done!")