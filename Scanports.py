#!/usr/bin/env python3
import socket, sys

if len(sys.argv) < 2:
    print("Brak parametrów. Wywołaj w formacie: ./Scanports.py HOST (-l)")
    exit()

if len(sys.argv) == 2:
    max_port = 1023
else:
    max_port = 65353
    
    
    
    
target_host = sys.argv[1]
#    target_host = "192.168.88.20"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
print("Testing " + target_host +"  porty: 1 - " + str(max_port))
    
for port in range(1,max_port):
    lokalizacja = (target_host, port)
    result_of_check = client.connect_ex(lokalizacja)
    if result_of_check == 0:
        print("Port " + str(port) + " OPEN")
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        result_of_check = 1
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
client.close()
    
