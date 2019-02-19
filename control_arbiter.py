import random
import time

import wifi_stream
import pwm_stream

def determine_priority(pwm_packet, wifi_packet):
	if pwm_packet['enable_override'] and not wifi_packet['enable_override']:
		return pwm_packet
	else:
		return wifi_packet

def control_arbiter_main():
	random.seed()

	pwm = pwm_stream.PwmStream()
	wifi = wifi_stream.WiFiStream()

	pwm_packet = wifi_packet = dict(pitch=0, yaw=0, roll=0, throttle=0, \
		enable_override=False, engage_hook=False)

	while True:
		pwm.generate_sample()
		wifi.generate_sample()

		pwm_packet = pwm.get_control_packet()
		if wifi.is_data_available():
			wifi_packet = wifi.get_control_packet()

		priority_packet = determine_priority(pwm_packet, wifi_packet)

		print("---pwm packet---")
		for key in pwm_packet:
			print(key + ": " + str(pwm_packet[key]))

		print("---wifi packet---")
		for key in wifi_packet:
			print(key + ": " + str(wifi_packet[key]))

		print("---priority packet---")
		for key in priority_packet:
			print(key + ": " + str(priority_packet[key]))

		time.sleep(1/60)

if __name__ == '__main__':
	control_arbiter_main()
