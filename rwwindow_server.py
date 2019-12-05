import socket
import time
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "test"

reservation = 50
weight = 5.0
win_size = 1.0

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    start_time = time.time()
    for i in range(reservation):
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        # random seperate
        time.sleep(random.random() / 10.0)
    while True:
        time.sleep(1.0 / weight)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        if (time.time() - start_time) >= win_size:
            start_time = time.time()
            break
    