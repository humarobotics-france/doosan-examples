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