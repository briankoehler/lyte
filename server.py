import socket
import os

class Server:
    socket_path = ""

    def __init__(self, socket_path: str):
        try:
            os.unlink(socket_path)
        except OSError:
            if os.path.exists(socket_path):
                raise
                
        self.socket_path = socket_path

    def start(self):
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(self.socket_path)
        server.listen(1)
        
        print('Server listening for incoming connections...')
        connection, client_address = server.accept()

        try:
            print(f'Connection from {str(connection).split(", ")[0][-4:]}')

            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f'Received data: {data.decode()}')

                response = 'Hello from the server!'
                connection.sendall(response.encode())
        finally:
            connection.close()
            os.unlink(self.socket_path)
