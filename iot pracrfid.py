
Import RPi.GPIO as GPIO
import time
import serial
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
greenLED=37
redLED=35
buzzer=33
GPIO.setup(greenLED,GPIO.OUT)
GPIO.setup(redLED,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(greenLED,False)
GPIO.output(redLED,False)
GPIO.output(buzzer,False)
#time.sleep(1)
def read_rfid():
    ser=serial.Serial("/dev/ttyUSB0")
    ser.baudrate=9600
    data=ser.read(12)
    ser.close()
    return data
try:
    while True:
        id=read_rfid()
        print (id)
        if id==b'1C0036B4DC42':
            print("access granted")
            GPIO.output(greenLED,True)
            GPIO.output(redLED,False)
            GPIO.output(buzzer,False)
        else:
            print("access denied")
            GPIO.output(greenLED,False)
            GPIO.output(redLED,True)
            GPIO.output(buzzer,True)
finally:
    GPIO.cleanup()

.






output :

