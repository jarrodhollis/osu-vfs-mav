#ifndef JSON_PARSER_HPP
#define JSON_PARSER_HPP

#include <string>
#include "jsmn.h"

class json_parser
{
	private:
		jsmn_parser parser;
		jsmntok_t *tokens;
		const char *json_string;
		unsigned int num_tokens_alloc;
		unsigned int num_tokens_read;
	protected:
		std::string get_token_string(int);
	public:
		json_parser(unsigned int);

		int parse_string(std::string);
		std::string get_string(std::string);
		int get_int(std::string);
		double get_double(std::string);
		bool get_bool(std::string);
};

#endif
