import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
freq = 1.0

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
start_time = time.time()

count = 0
while True:
    # start_time = time.time()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == "test":
        count = count + 1
    if (time.time() - start_time) >= freq:
        print count
        start_time = time.time()
        count = 0

