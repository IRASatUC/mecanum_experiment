#!/usr/bin/env python
from WaveShare_MotorHAT import WaveShare_MotorHAT, DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = WaveShare_MotorHAT(addr=0x40)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(WaveShare_MotorHAT.RELEASE)
    mh.getMotor(2).run(WaveShare_MotorHAT.RELEASE)
    mh.getMotor(3).run(WaveShare_MotorHAT.RELEASE)
    mh.getMotor(4).run(WaveShare_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor.run(WaveShare_MotorHAT.FORWARD);
# turn on motor
myMotor.run(WaveShare_MotorHAT.RELEASE);


while (True):
    print("Forward! ")
    myMotor.run(WaveShare_MotorHAT.FORWARD)

    print("\tSpeed up...")
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSlow down...")
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print("Backward! ")
    myMotor.run(WaveShare_MotorHAT.BACKWARD)

    print("\tSpeed up...")
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSlow down...")
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print("Release")
    myMotor.run(WaveShare_MotorHAT.RELEASE)
    time.sleep(1.0)
