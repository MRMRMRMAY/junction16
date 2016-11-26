# 1. Set serial console defines.py file and look through global assignments
# 2. Routine:
import iBeacon
from defines import *


if __name__ == '__main__':
	# Empty init
	beacon = iBeacon.Beacon()

	# Open serial communication
	beacon.open_connection(SERIAL_CONSOLE)

	#######################################################
	# Code goes here

	# Greeting function
	#beacon.greetings()

	# Control light level of all iBeacons (level -> 0..255)
	# beacon.set_light_level_all(level)

	# Control light level of individual iBeacons (vendor_id -> in defines.py)(level -> 0..255)
	# beacon.set_light_level_by_ID(vendor_id, level)

	#######################################################

	# Close serial communication
	beacon.close_connection()
