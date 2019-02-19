import random
import time

PULSE_WIDTH_MIN = 1.1
PULSE_WIDTH_MAX = 2.1

def generate_sample():
	control_packet = dict()
	control_packet['throttle'] = random.random()
	control_packet['pitch'] = random.uniform(-1, 1)
	control_packet['yaw'] = random.uniform(-1, 1)
	control_packet['roll'] = random.uniform(-1, 1)
	control_packet['engage_hook'] = random.choice([True, False])
	return control_packet

def translate_packet(control_packet):
	translated_packet = dict()
	translated_packet['motor_clockwise'] = linear_map(control_packet['throttle'] * 0.5 \
		+ control_packet['yaw'] * 0.5, 0, 1, PULSE_WIDTH_MIN, PULSE_WIDTH_MAX)
	translated_packet['motor_counterclockwise'] = linear_map(control_packet['throttle'] * 0.5 \
		- control_packet['yaw'] * 0.5, 0, 1, PULSE_WIDTH_MIN, PULSE_WIDTH_MAX)
	translated_packet['servo_pitch'] = control_packet['pitch']
	translated_packet['servo_roll'] = control_packet['roll']
	translated_packet['servo_hook'] = 2 * control_packet['engage_hook'] - 1
	return translated_packet

def linear_map(value, from_min, from_max, to_min, to_max):
	return (value - from_min) / (from_max - from_min) * (to_max - to_min) + to_min

def control_driver_main():
	random.seed()
	output_packet = dict(motor_clockwise=0, motor_counterclockwise=0, servo_pitch=0, \
		servo_roll=0, servo_hook=0)
	sample_available = False

	while True:
		if random.choice([True, False]):
			sample_available = True
			sample_packet = generate_sample()
			print("new sample")

		if sample_available:
			control_packet = sample_packet
			output_packet = translate_packet(control_packet)
			sample_available = False

		print("---sample packet---")
		for key in control_packet:
			print(key + ": " + str(control_packet[key]))

		print("---output packet---")
		for key in output_packet:
			print(key + ": " + str(output_packet[key]))

		time.sleep(3)

if __name__ == '__main__':
	control_driver_main()
