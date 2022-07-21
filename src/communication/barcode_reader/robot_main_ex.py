# -*- coding: utf-8 -*-
"""
An advance example of TCP/IP communication using a barcode scanner (main robot part)
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
What does this example: Use the TCPServer class to communicate with an computer
"""
barcode_reader = BarcodeReader()

while True:
    res, msg = barcode_reader.read()
    if res > 0:
        tp_popup("Barcode: " + str(msg))
    else:
        tp_popup("Not able to read the message")
