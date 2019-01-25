CC=clang++ -std=c++11 -g
EXE_FILE=vfs_main

all: $(EXE_FILE)

$(EXE_FILE): main.o jsmn.o json_parser.o pwm_stream.o wifi_stream.o
	$(CC) main.o jsmn.o json_parser.o pwm_stream.o wifi_stream.o -o $(EXE_FILE)

main.o: main.cpp
	$(CC) -c main.cpp

jsmn.o: jsmn.c
	$(CC) -c jsmn.c

json_parser.o: json_parser.cpp
	$(CC) -c json_parser.cpp

pwm_stream.o: pwm_stream.cpp
	$(CC) -c pwm_stream.cpp

wifi_stream.o: wifi_stream.cpp
	$(CC) -c wifi_stream.cpp

clean:
	rm -f *.o $(EXE_FILE)
