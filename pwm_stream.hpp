#ifndef PWM_STREAM_HPP
#define PWM_STREAM_HPP

#include "control_packet.hpp"

class pwm_stream
{
	private:
		control_packet current_packet;
		volatile double pitch_pwm;
		volatile double yaw_pwm;
		volatile double roll_pwm;
		volatile double throttle_pwm;
		volatile double override_pwm;
		volatile double hook_pwm;
	public:
		control_packet get_control_packet();
		void generate_sample();
};

#endif
