

#coding:utf-8
import serial
import time

ser =serial.Serial('/dev/ttyAMA0',115200)

def main():
    while True:
        count =ser.inWaiting()
        if count!=0:
            
            recv =ser.read(count)
            #print(count)
            print(recv)
            ser.write(recv)
        ser.flushInput()
        time.sleep(1)
        
if __name__=='__main__':
    try:
        main()
    except keyboardInterrupt:
        if ser!=None:
            ser.close()
