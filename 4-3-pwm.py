import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
duty_cycle = 0
t = 0
T = 10
try:
    while true:
        duty_cycle=float(input())
        t = duty_cycle*T
        GPIO.output(21, 3.3)
        timesleep(t)
        GPIO.output(21, 0)
        timesleep(T)
