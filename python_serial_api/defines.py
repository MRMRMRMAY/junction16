import serial

# console
SERIAL_CONSOLE='/dev/ttyUSB0'

# iBeacon configuration according to manual
SERIAL_BAUDRATE=19200			
SERIAL_PARITY=serial.PARITY_NONE
SERIAL_STOPBITS=serial.STOPBITS_ONE
SERIAL_FLOW_CONTROL=False

# delay between sequential write and read (seconds)
TIME_DELAY=0.2

# IDs
IBEACON_BROADCAST=0
IBEACON_1_ID=1
IBEACON_2_ID=2
IBEACON_3_ID=3


IBEACON_ARRAY_ALL = [IBEACON_1_ID, IBEACON_2_ID, IBEACON_3_ID]
IBEACON_ARRAY_REMOTE = IBEACON_ARRAY_ALL[1:]

# PYTHON HOST SYSTEM ID (currently does not matter)
HOST_ID = 0


# USERS FROM WEB INTERFACE
USER_RANDOM = 0
USER_RICHARD = 1
USER_KRISHJANIS = 2

USERS_MAC_ARRAY = ["44:74:6c:98:cc:d3", "c7:f5:0e:a2:ad:9c", "e5:8d:eb:89:ee:4d"]

RSSI_THRESH_MIN	= -100
RSSI_THRESH_MAX = -50

# Pink Flyd - time
AUDIO_TRACKS = [
["audio/space_odissey.mp3", "audio/Slash.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3"],
["audio/space_odissey.mp3", "audio/Slash.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3"],
["audio/space_odissey.mp3", "audio/Slash.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3", "audio/thunderstruck.mp3"]
]

