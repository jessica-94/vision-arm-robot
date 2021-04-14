import RPi.GPIO as GPIO    # utilisation GPIO

from time import time, sleep                      # utilisation time

GPIO.setmode(GPIO.BCM)     # numérotation BCM

in1 = 24
in2 = 23
en = 25
sa=2
sb=3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(sa, GPIO.IN)
GPIO.setup(sb, GPIO.IN)

p=GPIO.PWM(en,1000)
p.start(25)

eventCounter = 0

def my_callback(channel):
    global eventCounter
    if (x=='d'):
        eventCounter += 1
        print('position moteur 1:',eventCounter*1.155)
    if (x=='g'):
        eventCounter -= 1
        print('position moteur 1:',eventCounter*1.155)

x=input()   

GPIO.add_event_detect(sa, GPIO.RISING, callback=my_callback, bouncetime=3)
GPIO.add_event_detect(sb, GPIO.RISING, callback=my_callback, bouncetime=3)
      
while True:       # Jusqu'à CTRL+C
     
    x=input()
    if x=='r':
        print("run")
                
    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        
        x='z'
    
    elif x=='d':
        print("droite")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        p.ChangeDutyCycle(50)
                    
    elif x=='g':
        print("gauche")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        p.ChangeDutyCycle(100)

GPIO.cleanup()