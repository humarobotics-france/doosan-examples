# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication using a barcode scanner(Robot is the client)
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
import time
import sys
import os
import socket

class BarcodeReader:
    """Class of the TCP connection"""

    def __init__(self, ip="192.168.1.45", port=20002):
        """
        Initialize client

        Params:\n
            - 'ip': ip of the connection
            - 'port': port of the TCP connection
        """

        try:
            self.socket = client_socket_open(ip, port)
            tp_log("Connection ok!")
        except Exception as e:
            tp_popup("Socket connection failed. Error {0}".format(str(e)), DR_PM_ALARM)
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
        res, rx_data = client_socket_read(self.socket, length, timeout)

        # Check res value
        if res == -1:
            tp_log("error " + 
                "Error during a socket read: client not connected")
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

        res = client_socket_write(self.socket, msg)

        # Check res value
        if res == -1:
            tp_log("error " + 
                "Error during a socket write: client not connected")
        elif res == -2:
            tp_log("error " + "Error during a socket write: Socket error")
        elif res == 0:
            tp_log("info" + "Sending {0} command ok".format(msg))
        return res
