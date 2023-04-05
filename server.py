import socket
import threading
import json

# constants
HOST = '0.0.0.0'
PORT = 12345

# list to hold connected clients
clients = []

# function to handle incoming messages
def handle_client(client, addr):
    while True:
        try:
            # receive data from client
            data = client.recv(1024)
            if data:
                # parse JSON data
                message = json.loads(data.decode())
                
                # broadcast message to all clients
                for c in clients:
                    c.send(json.dumps(message).encode())
            else:
                # client disconnected
                client.close()
                clients.remove(client)
                break
        except:
            # an error occurred
            client.close()
            clients.remove(client)
            break

# function to start server
def start_server():
    # create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket to host and port
    server.bind((HOST, PORT))

    # listen for incoming connections
    server.listen()

    print(f"Server started on {HOST}:{PORT}")

    while True:
        # accept incoming connection
        client, addr = server.accept()
        
        # add client to list
        clients.append(client)
        
        # start thread to handle client
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.daemon = True
        thread.start()

# start server
start_server()
