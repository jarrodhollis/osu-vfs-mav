import random

class PwmStream:
	def __init__(self):
		self.pitch_pwm = 0.0
		self.yaw_pwm = 0.0
		self.roll_pwm = 0.0
		self.throttle_pwm = 0.0
		self.override_pwm = 0.0
		self.hook_pwm = 0.0
		self.current_packet = dict(pitch=0, yaw=0, roll=0, throttle=0, enable_override=False, engage_hook=False)

	def get_control_packet(self):
		self.current_packet['pitch'] = self.pitch_pwm
		self.current_packet['yaw'] = self.yaw_pwm
		self.current_packet['roll'] = self.roll_pwm
		self.current_packet['throttle'] = self.throttle_pwm
		self.current_packet['enable_override'] = True if self.override_pwm > 0.5 else False
		self.current_packet['engage_hook'] = True if self.hook_pwm > 0.5  else False
		return self.current_packet

	def generate_sample(self):
		self.pitch_pwm = random.random()
		self.yaw_pwm = random.random()
		self.roll_pwm = random.random()
		self.throttle_pwm = random.random()
		self.override_pwm = random.random()
		self.hook_pwm = random.random()
