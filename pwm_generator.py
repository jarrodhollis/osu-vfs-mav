from adafruit_servokit import ServoKit

def pwm_generator_main():
	kit = ServoKit(channels=16)
	kit.set_pwm_freq(60)
	kit.set_pwm(0, 0, 491)
	while True:
		True

if __name__ == '__main__':
	pwm_generator_main()
