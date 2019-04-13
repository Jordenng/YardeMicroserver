import socket
import requests
import time

class Server:

        HOST = "127.0.0.1"
        PORT = 8888
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))  # standard format for IPv4
        s.listen()  # enabling the server to accept connection
        connection, address = s.accept()  # returns connection and address from client
        while True:
                data = connection.recv(1024)
                if not data:
                        break
                connection.sendall(data)  # sending data received from client

        def get_request(self):
                url = "https://stackoverflow.com/"
                return requests.get(url)

        def post_with_delay(self):
                post_request = requests.post("https://stackoverflow.com", {'key':"value"}, time.sleep(0.1))
                time.sleep(1)
                return post_request

