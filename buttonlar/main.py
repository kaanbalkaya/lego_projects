#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
sembol_list='abcdefghijklmnopqrstvwxyz0123456789 .,:;*-+|<>'
i=-1
komut=''
# Write your program here.
ev3.speaker.beep()
ev3.screen.print("quit for quiting")
"""x=10             #koordinat x
y=0              #koordinat y
coll_pix=10
line_pix=10"""
while True:
    btn=ev3.buttons.pressed()
    if len(btn) !=0:
        if btn[0]== Button.DOWN:
            i+=1
            if(i>len(sembol_list)):
                i=-1
            ev3.screen.clear()
            #ev3.screen.draw_text(x, y, sembol_list[i])
            ev3.screen.print(komut,sembol_list[i])
        elif btn[0]==Button.RIGHT:
            komut+=sembol_list[i]
            i=-1
            ev3.screen.clear()
            #ev3.screen.draw_text(x, y, sembol_list[i])
            ev3.screen.print(komut)
            ##x+=coll_pix


        elif btn[0]==Button.LEFT:
            if len(komut)>0:
                #komut=komut.remove(len(komut)-1)
                komut=komut[:len(komut)-1]
                i=-1
                ev3.screen.clear()
                ev3.screen.print(komut)
            """if y!=0:
                y-=coll_pix"""
        elif btn[0]==Button.UP:
            if i!=-1:
                i-=1
            if(i<0):
                i=+1
            ev3.screen.clear()
            #ev3.screen.draw_text(x, y, sembol_list[i])
            ev3.screen.print(komut,sembol_list[i])
            #ev3.screen.print(sembol_list[i])
        elif btn[0]==Button.CENTER:
            f = os.popen(komut)
            result = f.read()
            if komut=="quit":
                break
            """x=0
            y+=line_pix"""        
            #ev3.screen.clear()
            #ev3.screen.draw_text(x, y, result)
            ev3.screen.print(result)
    wait(250)
