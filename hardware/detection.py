import time
import Rpi.GPIO as GPIO

#defining pins
TRIG = 7
ECHO = 12

#setting up pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)


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



