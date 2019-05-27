import socket
import time
import requests
#
class Client:

    # creating a client
    print("hello")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("0.0.0.0", 8888))  # connecting to server
    s.sendall(b'hello,world')  # sending server a message
    data = s.recv(1024)  # reading server replay

    def call_server_with_delay(self):
        get_request1 = requests.get("https://facebook.com", time.sleep(0.5))
        print(get_request1)
        post_request = requests.post("https://facebook.com", {'key':'value'},time.sleep(0.4))
        print(post_request)
        get_request2 = requests.get("https://stackoverflow.com", time.sleep(0.3))
        print(get_request2)

    # assignment 3 #

    def call_only_after_receving_response(self):
        get_response = requests.get("https://google.com")
        if get_response == 200:
            post_response = requests.post("https://google.com")
            if post_response == 200:
                requests.get("https://facebook.com")

    def response_status(self):
        request1 = requests.get("https://google.com")
        request2 = requests.get("https://apple.com")
        if request1.status_code == 200 and request2.status_code == 200:
            return request1, request2

