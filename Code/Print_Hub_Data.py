from pybricks import version
from micropython import opt_level, mem_info, qstr_info
import usys
from pybricks.hubs import PrimeHub

hub = PrimeHub(observe_channels=[0])

print(usys.implementation)
print(usys.version)
print(version)

info = hub.system.info()
print("Name: " + str(info["name"]))
print("Reset reason: " + str(info["reset_reason"]))
print("BLE connected: " + str(info["host_connected_ble"]))
print("Program start type: " + str(info["program_start_type"]))

mem_info(True)
qstr_info(True)

if info["reset_reason"] == 2:
    print("Rebooting from error")

print(" ________________________________")
print("|Information       |Value        |")
print("|------------------+-------------|")
print("|Battery voltage   |" + str(hub.battery.voltage()) + " mV     |")
print("|Battery current   |" + str(hub.battery.current()) + " mA     |")
print("|BLE version       |" + hub.ble.version() + "        |")
print("|BLE signal (ch 0) |" + str(hub.ble.signal_strength(0)) + " dBm   |")
print("'--------------------------------'")

if hub.charger.connected():
    if hub.charger.status() == 1:
        print("Charging")
    else:
        print("Battery full")