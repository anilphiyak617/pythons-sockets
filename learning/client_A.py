
import socket

#creating new socket object
client_socket=socket.socket()

port=9999
host_name=socket.gethostname()

#connect to the server on the specified port
client_socket.connect((host_name,port))

#sending data to the server
client_socket.send(bytes("This is the data from client_A",'utf-8'))

#recieve data from the server
data= client_socket.recv(1024)

print(data.decode())

client_socket.close()