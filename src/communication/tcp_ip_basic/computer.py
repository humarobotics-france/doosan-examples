# -*- coding: utf-8 -*-
"""
A basic example of TCP/IP communication
Copyright (C) 2021 HumaRobotics

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

On your computer you need:
    - Plug the computer to the robot
    - Run this python program

What does this example:
    1- Connect to the robot TCP/IP server
    2- Send a message to the robot
    3- Close the socket
"""
# source: https://python.doctor/page-reseaux-sockets-python-port

import socket

hote = "192.168.137.100"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

msg = "Hello world!"
emsg = msg.encode()
socket.send(emsg)

print("Close")
socket.close()