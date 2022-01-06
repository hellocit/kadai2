import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

p1 = GPIO.PWM(17, 50)
p2 = GPIO.PWM(18, 50)
p3 = GPIO.PWM(24, 50)
p4 = GPIO.PWM(25, 50)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

dr1=[0,25,50,75,100,75,50,25,0,0,0,0,0,0,0,0]
dr2=[0,0,0,0,0,0,0,0,25,50,75,100,75,50,25,0]
dr3=[0,25,50,75,100,75,50,25,0,0,0,0,0,0,0,0]
dr4=[0,0,0,0,0,0,0,0,25,50,75,100,75,50,25,0]

try:
        for i in range(16):
                    p1.ChangeDutyCycle(dr1[i])
                            p2.ChangeDutyCycle(dr2[i])
                                    p3.ChangeDutyCycle(dr3[i])
                                            p4.ChangeDutyCycle(dr4[i])
                                                    sleep(2)

except KeyboardInterrupt:
        pass

    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()

    GPIO.cleanup()
