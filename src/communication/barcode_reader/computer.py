# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication using a barcode scanner(Server part)
Copyright (C) 2022 HumaRobotics

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# source: https://python.doctor/page-reseaux-sockets-python-port
import socket
import threading
from time import sleep

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        
        print("[+] New thread for %s %s" % (self.ip, self.port))

    def close_socket(self):
        """ Close the client network socket"""
        self.clientsocket.close()
        print("Close client socket")
        
    def __del__(self):
        """ Destructor: close the client socket before close the program"""
        print("call __del__ function")
        self.close_socket()

    def recv(self, bufsize=255):
        """
        Read the socket

        Params:\n
            - 'bufsize': number of bytes to read (default = 255)

        Return:\n
            - 'response': data if data is received, None otherwise
        """
        response = b""
        while True:
            data = None
            try:
                data = self.clientsocket.recv(bufsize)
            except socket.timeout as e:
                print(e)
            except Exception as e:
                print("Socket connection failed. Error: {0}".format(
                str(e)))
                raise e
            if data:
                print("data", data)
                response += data
                if b"\r" in data:
                    response = response[:-1]
                    break
        
        return response.decode()

    def send(self, cmd):
        """
        Write 'cmd' in the socket

        Params:\n
            - 'cmd': command send to the client
        """
        # cmd += "\r"
        bytes_sent = self.clientsocket.send((cmd).encode())
        if len(cmd) != bytes_sent:
            print("Error during sending commande {0}, bytes_sent = {1}".format(cmd, bytes_sent))
            return -1
        return 0

    def run(self):

        print("Connexion de %s %s" % (self.ip, self.port, ))
        
        while True:
            barcode = input("Barcode: ")
            self.send(barcode)
            sleep(1)


def main():

    tcpsock = socket.socket()
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind(("", 20002))

    while True:
        tcpsock.listen(2)  # 2 connection max
        print("Listening...")
        (clientsocket, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsocket)
        newthread.start()


if __name__ == "__main__":
    main()


