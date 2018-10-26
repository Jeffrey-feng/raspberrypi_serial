#!/usr/bin/env python

import time
import serial

ser =serial.Serial('/dev/ttyAMA0',115200)
counter =0;
while 1:
    print(b'write counter :%d\n'%(counter))
    ser.write(b'write counter :%d\n'%(counter))
    time.sleep(1)
    counter+=1
    
    
    
