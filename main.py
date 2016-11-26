import bluepy.btle as ble
import configparser
import time

# Read user configuration file
config = configparser.ConfigParser()
config.read('user_config.ini')

# Create scanner object
scanner = ble.Scanner(0)

# Display scanned users
t = 0
while t<40:
    devices = scanner.scan(0.1)
    for d in devices:
            for user in config.sections():
                if d.addr==config[user]['MAC_address']:
                    print(user, "RSSI:", d.rssi)
    time.sleep(0.5)
    t += 1
