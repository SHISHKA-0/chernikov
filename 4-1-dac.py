import RPi.GPIO as GPIO
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(n):
    return[int(term) for term in bin(n)[2:].zfill(8)]

try:

    while(True):

        x=input()
        if x=='q':
              break
        elif  x.isdigit() and int(x)%1==0 and 0<=int(x)<=255:
                GPIO.output(dac,decimal2binary(int(x)))
                print("Напряжение, B: ", "{:.4f}".format(int(x)/256*3.3))
        elif  not x.isdigit() or int(x) not in range(0,256):
                print('Введите целое число от 0 до 255')

except ValueError:
    print('Введите целое число от 0 до 255!')

except KeyboardInterrupt:
    print('Готово')     
   
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()