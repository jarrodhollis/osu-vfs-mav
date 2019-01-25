#include <unistd.h>
#include <iostream>
#include "pwm_stream.hpp"
#include "wifi_stream.hpp"

#define NUM_TOKENS_ALLOC 128

control_packet determine_priority(control_packet, control_packet);
void print_control_packet(control_packet, std::string);

int main(int argc, char *argv[])
{
	srand(time(0));

	pwm_stream pwm;
	wifi_stream wifi(NUM_TOKENS_ALLOC);

	control_packet pwm_packet, wifi_packet;

	while (true)
	{
		pwm.generate_sample();
		wifi.generate_sample();
		pwm_packet = pwm.get_control_packet();
		if (wifi.is_data_available())
		{
			try
			{
				wifi_packet = wifi.get_control_packet();
			}
			catch (std::exception &e)
			{
				std::cout << e.what() << std::endl;
			}
		}
		control_packet priority_packet = determine_priority(pwm_packet, wifi_packet);

		print_control_packet(pwm_packet, "PWM Packet");
		print_control_packet(wifi_packet, "WiFi Packet");
		print_control_packet(priority_packet, "Priority Packet");

		usleep(3000000);

	}

	return 0;
}

control_packet determine_priority(control_packet pwm_packet, control_packet wifi_packet)
{
	if (pwm_packet.override || !wifi_packet.override)
	{
		return pwm_packet;
	}
	else
	{
		return wifi_packet;
	}
}

void print_control_packet(control_packet packet, std::string label)
{
	std::cout << label << std::endl
	<< "override: " << packet.override << std::endl
	<< "pitch: " << packet.pitch << std::endl
	<< "yaw: " << packet.yaw << std::endl
	<< "roll: " << packet.roll << std::endl
	<< "throttle: " << packet.throttle << std::endl
	<< "hook: " << packet.engage_hook << std::endl;
}
