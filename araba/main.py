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


# Create your objects here.
ev3 = EV3Brick()
ev3 = EV3Brick()
motor_sag=Motor(Port.A)
motor_sol=Motor(Port.D)
motor_sensor=Motor(Port.C)
infrared= InfraredSensor(Port.S1)

arac_donus=0.2093  ## 1 derece için aracın donerken kat ettiği yol cm  
teker_donus=0.034  ## 1 derece için tekerin donerken kat ettiği yol cm

# Write your program here.
ev3.speaker.beep()
while True:
    while (infrared.distance() > 50): 
        motor_sag.run(300)
        motor_sol.run(300)
    ##ev3.speaker.say("oooo oo") yavaslattı
    motor_sag.stop()
    motor_sol.stop()
    while (infrared.distance() <= 50): 
        motor_sensor.run_angle(200,10,wait=True)
        if motor_sensor.angle()>=359:
            motor_sensor.reset_angle(0)
            quit()
    kacis_acisi=motor_sensor.angle()
    yol=kacis_acisi*arac_donus
    teker_donus_acisi=yol/teker_donus
    if kacis_acisi<180:
        motor_sol.run_angle(360,teker_donus_acisi,wait=True)
    else:
        motor_sag.run_angle(360,teker_donus_acisi,wait=True)
    motor_sensor.run_angle(200,-1*kacis_acisi)    
    

#TODO: hız ve ivmeyi hesapla, ekranda göster
