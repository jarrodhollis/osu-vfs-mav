#include <cstdlib>
#include "pwm_stream.hpp"

control_packet pwm_stream::get_control_packet()
{
	current_packet.pitch = pitch_pwm;
	current_packet.yaw = yaw_pwm;
	current_packet.roll = roll_pwm;
	current_packet.throttle = throttle_pwm;
	current_packet.override = (override_pwm > 0.5);
	current_packet.engage_hook = (hook_pwm > 0.5);
	return current_packet;
}

void pwm_stream::generate_sample()
{
	pitch_pwm = ((double) rand()) / RAND_MAX;
	yaw_pwm = ((double) rand()) / RAND_MAX;
	roll_pwm = ((double) rand()) / RAND_MAX;
	throttle_pwm = ((double) rand()) / RAND_MAX;
	override_pwm = ((double) rand()) / RAND_MAX;
	hook_pwm = ((double) rand()) / RAND_MAX;
}
