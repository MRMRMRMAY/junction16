import time
import iBeacon
import bluepy.btle as ble

import urllib2

from player import *
from defines import *

# First person
# RANDOM
# RICHARDS
# KRISJANIS

# SleepZZZZZ
# 0() -> 4(sleepy)


# global variables
current_user = 0
current_mac = USERS_MAC_ARRAY[current_user]
current_rssi = RSSI_THRESH_MIN-1
current_sleepzzzz = 0
current_track = 0

# Define deligate object
class ScanDelegate(ble.DefaultDelegate):
        def __init__(self):
                ble.DefaultDelegate.__init__(self)
        
        def handleDiscovery(self, dev, isNewDev, isNewData):
                if dev.addr==current_mac:
                        print("Person has been detected")
                        global current_rssi
                        current_rssi = dev.rssi





def get_params_from_server():
        ret = []
        try:
               params = urllib2.urlopen("http://zzzyield.azurewebsites.net/state.php").read()
               params = params.split(" ")
               for i in params:
                       ret.append(int(i))
               return ret
        except:
               print("Connection lost!")
               ret.append(current_user)
               ret.append(current_sleepzzzz)
               ret.append(0) # Unused activity
               return ret



def test_api():
	beacon = iBeacon.Beacon()
	beacon.open_connection(SERIAL_CONSOLE)
	
	# Check validity
	beacon.ping_pong()

	# Go into read mode
	beacon.listen_mode()
	beacon.close_pconnection()


def get_light_level_from_rssi():
	if current_rssi > RSSI_THRESH_MAX:
		return 255
	elif current_rssi < RSSI_THRESH_MIN:
		return 0
	else:
		return abs(current_rssi)*(RSSI_THRESH_MAX-RSSI_THRESH_MIN)/255

def get_light_level_from_sleepzzzz():
	return current_sleepzzzz*51 + 51


def ligth_show():
        # beacon = iBeacon.Beacon()
        # beacon.open_connection(SERIAL_CONSOLE)
        # beacon.greetings()
        
        # Create bl scanner object
        scanner = ble.Scanner().withDelegate(ScanDelegate())
        player = Player()
        print("Ble scanner started")
        scanner.start()
        while(1):
                # Get user/slepenezzzzzz/activity
                params = get_params_from_server()
                
                # TODO check user is changed (reset)
                global current_user
                global current_mac
                global current_sleepzzzz
                current_user = params[0]
                current_mac = USERS_MAC_ARRAY[current_user]
                current_sleepzzzz = params[1]
                
                # SET SLEEPZZZZ LIGHT
                sleepzzz = get_light_level_from_sleepzzzz()
                print("Sleepz Light:", sleepzzz)
                # beacon.set_light_level_by_ID(IBEACON_1_ID, sleepzzz)
                
                print("Person: ", params[0])
                #print("Sleepzzzzzz: ", params[1])
                #print("Activity", params[2])
                
                # Armands scanner code
                scanner.process(2)
                #scanner.scan(1)
                
                # UPDATE MUSIC PLAYER
                player.setState(current_rssi >= RSSI_THRESH_MIN)
                player.update(current_user, current_sleepzzzz)
                
                # SET DISTANCE LIGHTS
                light_level = get_light_level_from_rssi()
                print("RSSI:", current_rssi)
                print("Distance Light:", light_level)
                # beacon.set_light_level_by_ID(IBEACON_2_ID, light_level)
                time.sleep(0.1)
                # beacon.set_light_level_by_ID(IBEACON_3_ID, light_level)
        
        # beacon.close_connection()


if __name__ == '__main__':
	#params = get_params_from_server()
	#print "Person: ", params[0]
	#print "Sleepzzzzzz: ", params[1]
	#print "Activity", params[2]
	ligth_show()
