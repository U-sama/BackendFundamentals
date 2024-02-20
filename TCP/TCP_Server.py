import socket

# Define the TCP server's IP address and port
TCP_IP = "127.0.0.1"
TCP_PORT = 8800

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
server_socket.listen(5)

print("TCP server is running...")

# Accept incoming connections indefinitely
while True:
    # Wait for a client to connect
    client_socket, addr = server_socket.accept()

    print(f"Connection established with {addr}")

    # Receive and respond to messages from the client
    while True:

        # Receive data from the client
        data = client_socket.recv(1024)

        if not data:
            break

        print(f"Received message: {data.decode()}")

        response = f"From server: {data.decode()}"

        # Echo the received message back to the client
        client_socket.sendall(response.encode())

        # Close the connection with the client

    client_socket.close()

# Close the server socket
server_socket.close()


########################
#client : ncat 127.0.0.1 8800 and send a message


