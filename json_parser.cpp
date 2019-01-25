#include <exception>
#include <iostream>
#include "json_parser.hpp"

std::string json_parser::get_token_string(int idx)
{
	return std::string(json_string + tokens[idx].start, tokens[idx].end - tokens[idx].start);
}

json_parser::json_parser(unsigned int num_tokens_alloc)
{
	this->num_tokens_alloc = num_tokens_alloc;
	tokens = new jsmntok_t[num_tokens_alloc];
	jsmn_init(&parser);
}

int json_parser::parse_string(std::string json_string)
{
	jsmn_init(&parser);
	this->json_string = json_string.c_str();
	int result = jsmn_parse(&parser, this->json_string, json_string.length(),
			tokens, num_tokens_alloc);
	num_tokens_read = (result > 0 ? result : 0);
	return result;
}

std::string json_parser::get_string(std::string key)
{
	for (int i = 0; i < num_tokens_read; i++)
	{
		if (get_token_string(i) == key && tokens[i + 1].type == JSMN_STRING)
		{
			return get_token_string(i + 1);
		}
	}
	throw std::runtime_error("token type is not string");
}

int json_parser::get_int(std::string key)
{
	for (int i = 0; i < num_tokens_read; i++)
	{
		if (get_token_string(i) == key && tokens[i + 1].type == JSMN_PRIMITIVE)
		{
			return std::stoi(get_token_string(i + 1));
		}
	}
	throw std::runtime_error("token type is not primitive");
}

double json_parser::get_double(std::string key)
{
	for (int i = 0; i < num_tokens_read; i++)
	{
		if (get_token_string(i) == key && tokens[i + 1].type == JSMN_PRIMITIVE)
		{
			return std::stod(get_token_string(i + 1));
		}
	}
	throw std::runtime_error("token type is not primitive 2");
}

bool json_parser::get_bool(std::string key)
{
	for (int i = 0; i < num_tokens_read; i++)
	{
		if (get_token_string(i) == key && tokens[i + 1].type == JSMN_PRIMITIVE)
		{
			if (get_token_string(i + 1) == "true")
			{
				return true;
			}
			else if (get_token_string(i + 1) == "false")
			{
				return false;
			}
			else
			{
				throw std::runtime_error("token data is not a boolean");
			};
		}
	}
	throw std::runtime_error("token type is not primitive 3");
}
