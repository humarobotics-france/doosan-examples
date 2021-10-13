# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication (main robot part)
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

What does this example: Use the TCPServer class to communicate with an computer
"""
computer = TCPServer()
res, msg = computer.read()
if res > 0:
    tp_log("Message from computer: " + str(msg))
else:
    tp_log("Not able to read the message")

computer.write("Hi")


while True:
    res, msg = computer.read()
    if res > 0 and msg != "":
        tp_log("Message from computer: " + str(msg))
        msg = msg.split(",")
        if msg[0] == "goto":
            computer.goto(msg[1:])
        elif msg[0] == "gotoj":
            computer.gotoj(msg[1:])
        elif msg[0] == "get_current_posj":
            computer.get_posj()
        elif msg[0] == "get_current_rotm":
            computer.get_rotm()
        elif msg[0] == "get_current_posx":
            computer.get_posx()

computer.close_socket()