import RPi.GPIO as GPIO
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(dac, GPIO.OUT)


# def waitForOpen():

#     print('GPIO initialized. Wait for door opening...')

#     # while GPIO.input(knop_in) >0:
#     #     pass
#     while True:
#         print(GPIO.input(24))


# waitForOpen()
GPIO.output(dac, 0)
GPIO.cleanup()


    