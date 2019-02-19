import random
import time

def data_processing_main():
	random.seed()
	sample_accel_gyro_available = False
	sample_sonar_available = False
	sonar_values = [0, 0, 0]
	accelerometer_values = [0, 0, 0]
	gyroscope_values = [0, 0, 0]

	while True:
		print("---iteration---")
		if random.choice([True, False]):
			sample_accel_gyro_available = True
			for idx, member in enumerate(accelerometer_values):
				accelerometer_values[idx] = random.uniform(0, 10)
			for idx, member in enumerate(gyroscope_values):
				gyroscope_values[idx] = random.uniform(-90, 90)

		if random.choice([True, False]):
			sample_sonar_available = True
			for idx, member in enumerate(sonar_values):
				sonar_values[idx] = random.uniform(5, 300)

		if sample_accel_gyro_available:
			sample_accel_gyro_available = False
			data_packet = dict()
			data_packet['type'] = "accel/gyro"
			data_packet['accel_x'] = accelerometer_values[0]
			data_packet['accel_y'] = accelerometer_values[1]
			data_packet['accel_z'] = accelerometer_values[2]
			data_packet['gyro_x'] = gyroscope_values[0]
			data_packet['gyro_y'] = gyroscope_values[1]
			data_packet['gyro_z'] = gyroscope_values[2]

			print("---data packet---")
			for key in data_packet:
				print(key + ": " + str(data_packet[key]))

		if sample_sonar_available:
			sample_sonar_available = False
			data_packet = dict()
			data_packet['type'] = "sonar"
			data_packet['sonar_1'] = sonar_values[0]
			data_packet['sonar_2'] = sonar_values[1]
			data_packet['sonar_3'] = sonar_values[2]

			print("---data packet---")
			for key in data_packet:
				print(key + ": " + str(data_packet[key]))

		time.sleep(3)

if __name__ == '__main__':
	data_processing_main()
