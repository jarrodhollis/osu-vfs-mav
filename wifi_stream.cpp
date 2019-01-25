#include <cstdlib>
#include <iostream>
#include "wifi_stream.hpp"

wifi_stream::wifi_stream(unsigned int num_tokens) : parser(num_tokens)
{
	data_available = false;
	data_string = "";
}

bool wifi_stream::is_data_available()
{
	return data_available;
}


control_packet wifi_stream::get_control_packet()
{
	if (data_available)
	{
		data_available = false;

		if (parser.parse_string(data_string))
		{
			std::cout << data_string << std::endl;
			current_packet.override = parser.get_bool("enable_override");
			current_packet.pitch = parser.get_double("pitch");
			current_packet.yaw = parser.get_double("yaw");
			current_packet.roll = parser.get_double("roll");
			current_packet.throttle = parser.get_double("throttle");
			current_packet.engage_hook = parser.get_bool("engage_hook");
		}
		else
		{
			throw std::runtime_error("could not parse data string");
		}
	}

	return current_packet;
}

void wifi_stream::generate_sample()
{
	data_string = std::string("{ \"enable_override\": ") + std::string(rand() % 2 ? "true" : "false")
			+ std::string(", \"pitch\": ") + std::to_string(((double) rand()) / RAND_MAX)
			+ std::string(", \"yaw\": ") + std::to_string(((double) rand()) / RAND_MAX)
			+ std::string(", \"roll\": ") + std::to_string(((double) rand()) / RAND_MAX)
			+ std::string(", \"throttle\": ") + std::to_string(((double) rand()) / RAND_MAX)
			+ std::string(", \"engage_hook\": ") + std::string(rand() % 2 ? "true" : "false") + std::string(" }");
	data_available = true;
}
