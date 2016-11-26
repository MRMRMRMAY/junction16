import time
import iBeacon

import urllib2

from defines import *

# First person
# RANDOM
# RICHARDS
# KRISJANIS

# SleepZZZZZ
# 0() -> 4(sleepy)

def get_params_from_server():
	ret = []
	params = urllib2.urlopen("http://zzzyield.azurewebsites.net/state.php").read()
	params = params.split(" ")
	for i in params:
		ret.append(int(i))
	return ret



def test_api():
	beacon = iBeacon.Beacon()
	beacon.open_connection(SERIAL_CONSOLE)
	
	# Check validity
	beacon.ping_pong()

	# Go into read mode
	beacon.listen_mode()
	beacon.close_connection()


def ligth_show():
	beacon = iBeacon.Beacon()
	beacon.open_connection(SERIAL_CONSOLE)
	beacon.greetings()

	# Get user/slepenezzzzzz/activity
	params = get_params_from_server()
	print "Person: ", params[0]
	print "Sleepzzzzzz: ", params[1]
	print "Activity", params[2]

	# Armands scanner code



	beacon.close_connection()


if __name__ == '__main__':
	#params = get_params_from_server()
	print "Person: ", params[0]
	print "Sleepzzzzzz: ", params[1]
	print "Activity", params[2]
	#ligth_show()
