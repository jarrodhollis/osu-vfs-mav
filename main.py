import time
import spidev
import board
import busio
import adafruit_pca9685
import time

PULSE_WIDTH_MIN = 1.1
PULSE_WIDTH_MAX = 2.1

def linear_map(value, from_min, from_max, to_min, to_max):
	return (value - from_min) / (from_max - from_min) * (to_max - to_min) + to_min

def main():
	# bonnet config
	i2c = busio.I2C(board.SCL, board.SDA)
	hat = adafruit_pca9685.PCA9685(i2c)
	hat.frequency = 60
	pwm_cw_channel = hat.channels[0]
	pwm_ccw_channel = hat.channels[1]

	# spi config
	spi = spidev.SpiDev()
	spi.open(0, 0)
	spi.max_speed_hz = 7629

	while True:
		# read input
		thrust_pwm = spi.readbytes(4)
		yaw_pwm = spi.readbytes(4)

		# translate output
		thrust = linear_map(thrust_pwm, 0.0011, 0.002, 0, 1)
		yaw = linear_map(yaw_pwm, 0.0011, 0.002, -1, 1)

		# Matt: multiply these expressions to scale, keep in range of 0-1
		cw_pwm = (0.0009 * thrust / 2 * 2 * (1 + yaw) + 0.0011)
		ccw_pwm = (0.0009 * thrust / 2 * 2 * (1 - yaw) + 0.0011)

		# drive PWM bonnet
		pwm_cw_channel.duty_cycle = linear_map(cw_pwm, 0.0011, 0.002, 4325, 7864)
		pwm_ccw_channel.duty_cycle = linear_map(cw_pwm, 0.0011, 0.002, 4325, 7864)

if __name__ == '__main__':
	main()
