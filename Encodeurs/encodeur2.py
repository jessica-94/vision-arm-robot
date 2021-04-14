import RPi.GPIO as GPIO    # utilisation GPIO

from time import time, sleep                      # utilisation time

GPIO.setmode(GPIO.BCM)     # numérotation BCM

in3 = 6
in4 = 26
en2 = 5
sa=20
sb=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.setup(sa, GPIO.IN)
GPIO.setup(sb, GPIO.IN)

q=GPIO.PWM(en2,1000)
q.start(25)

eventCounter = 0

def my_callback(channel):
    global eventCounter
    eventCounter += 1
    print(eventCounter)

x=input()   

GPIO.add_event_detect(sa, GPIO.RISING, callback=my_callback, bouncetime=3)
   

      
while True:       # Jusqu'à CTRL+C
     
    x=input()
    if x=='r':
        print("run")
                
    elif x=='s':
        print("stop")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
        x='z'
    
    elif x=='h':
        print("haut")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        q.ChangeDutyCycle(100)
        x='z'
                    
    elif x=='b':
        print("bas")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        q.ChangeDutyCycle(50)
        x='z'

GPIO.cleanup()