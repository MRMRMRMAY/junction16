import serial
import time
import sys

from defines import *
from optcodes import *



class Beacon():
	def open_connection(self, serial_console):
		# serial configuration
		self.serial_connection = serial.Serial(
			port	=serial_console,
			baudrate=SERIAL_BAUDRATE,					
			parity 	=SERIAL_PARITY,
			stopbits=SERIAL_STOPBITS,
			xonxoff =SERIAL_FLOW_CONTROL
		)

		if (self.serial_connection.isOpen() == False):
			print("Connection not open!")

	def close_connection(self):
		self.serial_connection.close()

	def send_byte_array(self, byte_array):
		input = str(byte_array)
		self.serial_connection.write(input);

	def send_message(self, msg_array):
		msg_array.insert(0,len(msg_array))
		input = str( bytearray(msg_array) )
		self.serial_connection.write(input);

	def read_message(self):
		message = ''
		# read length (first byte)
		length = ord(self.serial_connection.read(1))

		# bytes still to recieve
		tmp = length
		while(tmp > 0):
			# wait for bytes in buffer
			while( self.serial_connection.inWaiting()==0 ): 1

			# add bytes to message
			message += self.serial_connection.read(1)
			
			# iterator
			tmp = tmp -1;

		return [length, message]

	# routine check send: 0x1 0x1; return: 0x1 0x2
	def ping_pong(self):
		self.send_byte_array( bytearray([0x1, 0x1]) )
		time.sleep(TIME_DELAY)
		out = self.read_message()

	# set lightning level 0..255
	def set_lightning_level_local(self, level):
		self.send_byte_array( bytearray([0x2, 0x13, level]) )
	
	def debug_print_message(self, length, message):
		print("Length ", length , "Message-> "),
		for i in message:
			print("0x" + i.encode("hex")),
		print('')

	def listen_mode(self):
		while(1):
			[length, msg] = self.read_message()
			self.debug_print_message(length, msg)




	# Public methods
	def set_light_level_by_ID(self, vendor_id, level):
		# this is local iBeacon -> can use plain CMB command
		if vendor_id == IBEACON_1_ID:
			self.set_lightning_level_local(level)
		else:
			# not local iBeacon -> send network message
			message = [CMB_VENDORMESSAGE0, HOST_ID, vendor_id, VENDOR_CMD_SET_LIGHT, level];
			self.send_message(message)

	def set_light_level_all(self, level):
		# set local light level
		self.set_lightning_level_local(level)

		# broadcast network light level
		message = [CMB_VENDORMESSAGE0, HOST_ID, IBEACON_BROADCAST, VENDOR_CMD_SET_LIGHT, level];
		self.send_message(message)

	def greetings(self):
		self.set_light_level_all(0)
		time.sleep(0.3)
		i = 24
		
		while(i):
			self.set_light_level_all(i*10)
			time.sleep(0.2)
			i = i-4

		self.set_light_level_all(30)







