#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
"""
motor_sag=Motor(Port.A)
motor_sol=Motor(Port.D)
motor_sensor=Motor(Port.C)
infrared= InfraredSensor(Port.S1)
class DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
"""

# Create your objects here.
ev3 = EV3Brick()
drive_base=DriveBase(Motor(Port.D),Motor(Port.A),20,90)
infrared= InfraredSensor(Port.S1)
motor_sensor=Motor(Port.C)

# Write your program here.
ev3.speaker.beep()

while True:
    drive_base.drive(100,0)
    while (infrared.distance() <= 50): 
        drive_base.stop()
        motor_sensor.run_angle(200,10,wait=True)
        if motor_sensor.angle()>=359:
            motor_sensor.reset_angle(0)
            quit()
        kacis_acisi=motor_sensor.angle()
        drive_base.turn(kacis_acisi)
        motor_sensor.run_angle(200,-1*kacis_acisi)    
    
    
