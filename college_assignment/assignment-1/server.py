import socket

HOST = 'localhost'  # Set to whichever IP address you want to listen on
PORT = 5000  # Set to whichever port you want to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to a specific IP address and port
    server_socket.bind((HOST, PORT))

    # Start listening for incoming connections
    server_socket.listen()

    print(f'Server listening on {HOST}:{PORT}')

    while True:
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()

        print(f'Client connected from {client_address}')

        # Receive data from the client
        data = client_socket.recv(1024)

        # Echo the data back to the client
        client_socket.sendall(data)

        # Close the connection with the client
        client_socket.close()
