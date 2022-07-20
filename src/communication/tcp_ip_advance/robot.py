# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication (TCPServer class part)
Copyright (C) 2021 HumaRobotics

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

import time
import sys
import os
import socket

class TCPServer:
    """Class of the TCP connection"""

    def __init__(self, port=20002):
        """
        Initialize server

        Params:\n
            - 'port': port of the TCP connection
        """

        try:
            self.socket = server_socket_open(port)
            tp_log("Connection ok!")
        except Exception as e:
            tp_popup("Socket connection failed. Error {0}".format(str(e)), DR_PM_ALARM)
            raise e

    def close_socket(self):
        """ Close the network socket"""
        try:
            server_socket_close(self.socket)
            tp_log("Close the socket")
        except Exception as e:
            tp_log("Socket connection was not closed. Error: {0}".format(str(e)))
            raise e

    def read(self, length=-1, timeout=-1):
        """
        Read the socket

        Params:\n
            - 'length': number of bytes to read (default = -1)
            - 'timeout': Waiting time (default = -1)

        Return:\n
            - 'res': result of the reading
            - 'rx_data': data received
        """
        res, rx_data = server_socket_read(self.socket, length, timeout)

        # Check res value
        if res == -1:
            tp_log("error " + 
                "Error during a socket read: Server not connected")
        elif res == -2:
            tp_log("error " + "Error during a socket read: Socket error")
        elif res == -3:
            tp_log("error " + 
                "Error during a socket read: Waiting time has expired")
        elif res > 0:
            if rx_data != "":
                tp_log("info" + 
                    "Read res = {0} and rx_data = {1}".format(res, rx_data))
                rx_data = rx_data[:-1]
                rx_data = rx_data.decode()

        return res, rx_data

    def write(self, msg):
        """
        Write 'msg' in the socket

        Params:\n
            - 'msg': a message

        Return:\n
            - 'res': result of the writing

        Exemple:\n
            write("posj(100,100,100,100,100,100)")
        """
        msg = msg + "\r"
        # Convert msg in ascii before sending
        msg = bytes(msg, encoding="ascii")

        res = server_socket_write(self.socket, msg)

        # Check res value
        if res == -1:
            tp_log("error " + 
                "Error during a socket write: Server not connected")
        elif res == -2:
            tp_log("error " + "Error during a socket write: Socket error")
        elif res == 0:
            tp_log("info" + "Sending {0} command ok".format(msg))
        return res

    def goto(self, msg_pos):
        """ goto """
        tp_log("debug " + "goto")
        p = [float(elem) for elem in msg_pos]
        movel(p, vel=80, acc=50)
        self.write("goto,done")

    def gotoj(self, msg_posj):
        """ gotoj """
        tp_log("debug " + "gotoj")
        p = [float(elem) for elem in msg_posj]
        movej(p, vel=80, acc=50)
        self.write("gotoj,done")

    def get_posj(self):
        """ get_posj """
        tp_log("debug " + "get_posj")
        current_posj = get_current_posj()
        msg = "posj," + str(current_posj).replace(']','').replace('[','')
        self.write(msg)

    def get_posx(self):
        """ get_posx """
        tp_log("debug " + "get_posx")
        posx, sol_space = get_current_posx()
        msg = "posx," + str(posx).replace(']','').replace('[','') + ',' + str(sol_space)
        self.write(msg)