<a href="https://www.humarobotics.com/">
    <img src="../../../images/Logo_HR_bleu.png" alt="HumaRobotics logo" title="HumaRobotics" align="right" height="80" />
</a>

# TCP/IP advance example

An advance example of TCP/IP communication between a Doosan and a computer. The computer can send order to the robot (goto, gotoj, get_current_posj, etc).

## How to use

- Connect the computer to the robot with an ethernet cable
- Configure the network of the computer to match the network of the robot
- Create a task writer and import the [robot.py](./robot.py) program in a CustomCode before the MainSub.
- Create another CustomCode with [robot_main.py](./robot_main.py) inside
- Start robot program
- Run `python computer.py` on the computer
