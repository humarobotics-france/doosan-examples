# -*- coding: utf-8 -*-
"""
A basic example of TCP/IP communication
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