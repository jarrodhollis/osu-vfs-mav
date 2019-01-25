#ifndef WIFI_STREAM_HPP
#define WIFI_STREAM_HPP

#include "json_parser.hpp"
#include "control_packet.hpp"

class wifi_stream
{
	protected:
		json_parser parser;
		bool data_available;
		std::string data_string;
		control_packet current_packet;
	public:
		wifi_stream(unsigned int);
		bool is_data_available();
		control_packet get_control_packet();
		void generate_sample();
};

#endif
