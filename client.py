import socket
import json

class TetrisClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_connected = False

    def connect(self):
        self.socket.connect((self.server_ip, self.server_port))
        self.is_connected = True

    def disconnect(self):
        self.socket.close()
        self.is_connected = False

    def send_message(self, message):
        message_json = json.dumps(message)
        message_bytes = message_json.encode()
        self.socket.sendall(message_bytes)

    def receive_message(self):
        message_bytes = self.socket.recv(4096)
        message_json = message_bytes.decode()
        message = json.loads(message_json)
        return message
