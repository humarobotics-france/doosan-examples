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

In your Task Writer/ Task Builder you need:
    - A 'CustomCode' with this file

What does this example:
    1- Start a TCP/IP server on port 15555
    2- Wait for a message from a client
    3- Display the message in a popup
    4- Close the socket TCP/IP
"""
port = 15555
socket = server_socket_open(port)
res, rx_data = server_socket_read(socket)
rx_data = rx_data.decode()
tp_popup("Receive message: {}".format(rx_data))


server_socket_close(socket)