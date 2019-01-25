#ifndef CONTROL_PACKET_HPP
#define CONTROL_PACKET_HPP

struct control_packet
{
	bool override = false;
	double pitch = 0;
	double yaw = 0;
	double roll = 0;
	double throttle = 0;
	bool engage_hook = false;
};

#endif
