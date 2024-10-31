import RPi.GPIO as GPIO
from time import sleep
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(n):
    return[int(e) for e in bin(n)[2:].zfill(8)]

try:
    t = int(input())
    while True:
        for i in range(0, 256):
            GPIO.output(dac, decimal2binary(i))
            print(i,"Напряжение ",'\n', "{:.4f}".format(3.3*i/256))
            sleep(t / 512)
        for i in range(0,256):
            GPIO.output(dac, decimal2binary(255-i))
            print(255-i,"Напряжение ",'\n', "{:.4f}".format(3.3*(255-i)/256))
            sleep(t / 512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
