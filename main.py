import bluepy.btle as ble
import configparser
import time

# Read user configuration file
config = configparser.ConfigParser()
config.read('user_config.ini')

# Define deilgate object funtions
class ScanDelegate(ble.DefaultDelegate):
    def __init__(self):
        ble.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        for user in config.sections():
            if dev.addr==config[user]['MAC_address']:
                print(user, "RSSI", dev.rssi)
scanner.start()
scanner.process(10)

