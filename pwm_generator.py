import board
import busio
import adafruit_pca9685


def pwm_generator_main():
	i2c = busio.I2C(board.SCL, board.SDA)
	hat = adafruit_pca9685.PCA9685(i2c)
	hat.frequency = 60
	pwm_channel = hat.channels[0]

	while True:
		pwm_channel.duty_cycle = 4325
		time.sleep(3)
		pwm_channel.duty_cycle = 7864
		time.sleep(3)

if __name__ == '__main__':
	pwm_generator_main()
