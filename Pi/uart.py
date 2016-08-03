#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=0.5)

def openPort():
    print 'Opening port'    
    if not ser.isOpen():
        ser.open()
    print 'is port open?'
    print ser.isOpen()

def closeport():
    print 'closing serial port'
    ser.close()
    print 'Done'

def sendData(data):
    try:
        ser.write(data + '\n\r')       
    except:
        print 'error while writting to serial port'




