import random
import json

class WiFiStream:

	def __init__(self):
		self.data_available = False
		self.data_string = ""
		self.current_packet = dict(pitch=0, yaw=0, roll=0, throttle=0, \
			enable_override=False, engage_hook=False)

	def is_data_available(self):
		return self.data_available

	def get_control_packet(self):
		self.data_available = False
		temp_packet = json.loads(self.data_string)
		self.current_packet['pitch'] = temp_packet['pitch']
		self.current_packet['yaw'] = temp_packet['yaw']
		self.current_packet['roll'] = temp_packet['roll']
		self.current_packet['throttle'] = temp_packet['throttle']
		self.current_packet['enable_override'] = temp_packet['enable_override']
		self.current_packet['engage_hook'] = temp_packet['engage_hook']
		return self.current_packet

	def generate_sample(self):
		self.data_string = "{ \"pitch\": " + str(random.random()) \
			+ ", \"yaw\": " + str(random.random()) \
			+ ", \"roll\": " + str(random.random()) \
			+ ", \"throttle\": " + str(random.random()) \
			+ ", \"enable_override\": " + random.choice(["true", "false"]) \
			+ ", \"engage_hook\": " + random.choice(["true", "false"]) + " }"
		self.data_available = True
