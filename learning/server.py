import socket;

server_socket=socket.socket()

print('server socket created')

PORT=9999
HOST_NAME=socket.gethostname()

#localhost binds the server to loopback interface or local interface 
#server will accept connections from the same machine 
server_socket.bind((HOST_NAME,PORT))

server_socket.listen(3)
print("listening ate port {PORT}, waiting for connection")


while True:
    # establish a connection server_
    # socket.accept() accepts the incoming request from client
    #  returns new tuple[socket object,socket_adress]
    client_socket,address=server_socket.accept()

    print("connected with",address)

    while True:
        data=client_socket.recv(1024)

        #if the data is not recieved i.e client has disconnected, break the loop
        if not data:
            break

        print(data.decode())
        client_socket.sendall(bytes("welcome to Socket programming in python",'utf-8'))
    


    client_socket.close()