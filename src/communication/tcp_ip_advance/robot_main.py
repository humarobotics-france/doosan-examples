# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication (main robot part)

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