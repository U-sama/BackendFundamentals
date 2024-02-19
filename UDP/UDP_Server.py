import socket

# Define the UDP server's IP address and port
UDP_IP = "127.0.0.1"
UDP_PORT = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))

print("UDP server is running...")

# Listen for incoming data indefinitely
while True:
    # Receive data from the client
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print(f"Received message: {data.decode()} from {addr}")

    # Echo the received message back to the client
    sock.sendto(data, addr)

###############
    #Usage
    # CMD: ncat -u 127.0.0.1 8080
