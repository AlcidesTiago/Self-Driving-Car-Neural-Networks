#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MainRobotLane.py
#
#  Copyright 2021 Alcides Fernando Tiago <alcidesft6@gmail.com>
#  MA 02110-1301, USA.
#
#
from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
import cv2

##################################################
motor = Motor(2, 3, 4, 17, 22, 27)
##################################################

def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    maxVAl = 0.3 # MAX SPEED
    if curveVal > maxVAl: curveVal = maxVAl
    if curveVal < -maxVAl: curveVal = -maxVAl
    # print(curveVal)
    if curveVal > 0:
        sen = 1.7
        if curveVal < 0.03: curveVal = 0
    else:
        if curveVal > -0.08: curveVal = 0
    motor.move(0.25, -curveVal * sen, 0.05)
    cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()
