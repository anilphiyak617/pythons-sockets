import socket

HOST = 'localhost'  # Set to the IP address of the server
PORT = 5000  # Set to the port the server is listening on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))

    while True:
        # Send data to the server
        message = input('Enter a message to send to the server: ')
        client_socket.send(message.encode())

        # Receive data from the server
        data = client_socket.recv(1024)

        print(f'Server sent back: {data.decode()}')
