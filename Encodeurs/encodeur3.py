import RPi.GPIO as GPIO    # utilisation GPIO

from time import time, sleep                      # utilisation time

GPIO.setmode(GPIO.BCM)     # numérotation BCM

in5 = 27
in6 = 22
en3 = 17
sa=1
sb=7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.setup(sa, GPIO.IN)
GPIO.setup(sb, GPIO.IN)

j=GPIO.PWM(en3,1000)
j.start(25)

eventCounter = 0

def my_callback(channel):
    global eventCounter
    eventCounter += 1
    print(eventCounter)

x=input()   

GPIO.add_event_detect(sa, GPIO.RISING, callback=my_callback, bouncetime=3)
   

      
while True:       # Jusqu'à CTRL+C
    print(eventCounter) 
    x=input()
    if x=='r':
        print("run")
                
    elif x=='s':
        print("stop")
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        
        x='z'
    
    elif x=='ar':
        print("arriere")
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        j.ChangeDutyCycle(50)
        x='z'
                    
    elif x=='av':
        print("avant")
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        j.ChangeDutyCycle(50)
        x='z'

GPIO.cleanup()