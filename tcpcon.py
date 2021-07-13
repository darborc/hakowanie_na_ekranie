#!/usr/bin/env python3
import socket, sys

if len(sys.argv) < 3:
    print("Brak parametrów. Wywołaj w formacie: ./tcpcon.py HOST PORT")
    exit()
    
else:
    target_host = sys.argv[1]
    target_port = int(sys.argv[2])

    lokalizacja = (target_host, target_port)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = client.connect_ex(lokalizacja)


    print("Testing " + target_host + " on port " + str(target_port))

    if result_of_check == 0:
        print("Port OPEN")
    else:
        print("Port CLOSED")
    
    client.close()
    
        