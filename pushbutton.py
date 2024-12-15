import serial
import time
import os

d = serial.Serial("/dev/pushbutton")
while True:
    while d.in_waiting == 0:
        time.sleep(1)
    os.system("/bin/sh -c 'echo hello world!'") # change this to be used for invoking a command upon push button being pressed!
    d.read(d.in_waiting)
    time.sleep(1)
