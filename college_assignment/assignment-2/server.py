import socket
import threading

HOST = 'localhost' # The servers hostname of IP
PORT=5000          # The port to be used by the server

def handle_client(conn,address):
    """handles a single client connnection.
    :param conn: the client's socket object
    :param address: the client's adress tuple {ip,port}
    """

    print(f"New connection from {address}")

    while True:

        data=conn.recv(1024)
        if not data:
            break

        message=data.decode('utf-8')
        print(f"Recieved message from {address}:{message}")

        #
        response= f"You :{message}"
        conn.sendall(response.encode('utf-8'))

    print(f"Connection from {address} closed.")
    conn.close()




def start_server():

    #Create a new Object
    with socket.socket() as server_socket:
        #Bind the socket to a specifice adress and port
        server_socket.bind((HOST,PORT))

        #Listen for incoming connection
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        # Waiting for the incoming connection from the client
        while True:
            conn,address=server_socket.accept()

            client_thread=threading.Thread(target=handle_client,args=(conn,address))
            client_thread.start()


if __name__=='__main__':
    start_server()