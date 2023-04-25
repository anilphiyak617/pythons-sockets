import socket


HOST = 'localhost'
PORT =5000

#create a socket object
client_socket=socket.socket()

#connect to thr server
client_socket.connect((HOST,PORT))

print(__name__)

while True:

    #taker user input
    message=input('Type your message: ')
    #send data to the server
    client_socket.sendall(message.encode("utf-8"))

     # Receive data from the server
    data = client_socket.recv(1024)

    print(f'Server sent back: {data.decode("utf-8")}')


# client_socket.close()

