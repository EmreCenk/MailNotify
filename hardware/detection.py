import time
import Rpi.GPIO as GPIO

#defining pins
TRIG = 7
ECHO = 12
LED = 25

#setting up pins
GPIO.setup(LED,GPIO.OUT)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

while True:
    #firing the ultrasonic wave
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time();

    #calculation

    distance = (stop-start) * 17000
    print (distance)

    #Decision

    if distance >= 3:
        time.sleep(0.25)

    elif distance < 3:
        GPIO.output(LED, 1)

        # PUT CAMERA OPERATION HERE
        # please add delay here as well if you havent.

        GPIO.output(LED, 0)

    GPIO.cleanup()



