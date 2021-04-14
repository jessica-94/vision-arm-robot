import RPi.GPIO as GPIO
from time import sleep
in1 = 24
in2 = 23
en = 25

in3 = 6
in4 = 26
en2 = 5

in5 = 27
in6 = 22
en3 = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)


GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)


p=GPIO.PWM(en,1000)
p.start(25)

q=GPIO.PWM(en2,1000)
q.start(25)

j=GPIO.PWM(en3,1000)
j.start(25)


print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")
while(1):
    x=input()
    if x=='r':
        print("run")
                
    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'
        
    elif x=='d':
        print("droite")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        p.ChangeDutyCycle(50)
        sleep(0.4)
        p.ChangeDutyCycle(0)
        x='z'
                    
    elif x=='g':
        print("gauche")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        p.ChangeDutyCycle(50)
        sleep(0.4)
        p.ChangeDutyCycle(0)
        x='z'
        
    elif x=='h':
        print("haut")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        q.ChangeDutyCycle(100)
        sleep(0.6)
        q.ChangeDutyCycle(0)
        x='z'
                    
    elif x=='b':
        print("bas")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        q.ChangeDutyCycle(50)
        sleep(0.4)
        q.ChangeDutyCycle(0)
        x='z'
        
    elif x=='ar':
        print("arriere")
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        j.ChangeDutyCycle(50)
        sleep(0.2)
        j.ChangeDutyCycle(0)
        x='z'
                    
    elif x=='av':
        print("avant")
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        j.ChangeDutyCycle(50)
        sleep(0.2)
        j.ChangeDutyCycle(0)
        x='z'
                            
    elif x=='e':
        GPIO.cleanup()
        break
    
    elif x=='t':
        print("toute direction")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        q.ChangeDutyCycle(100)
        sleep(0.6)
        q.ChangeDutyCycle(0)
        
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        p.ChangeDutyCycle(50)
        sleep(0.4)
        p.ChangeDutyCycle(0)
        
        
        print("bas")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        q.ChangeDutyCycle(50)
        sleep(0.4)
        q.ChangeDutyCycle(0)
        
        
        print("bas")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        q.ChangeDutyCycle(50)
        sleep(0.4)
        q.ChangeDutyCycle(0)
        
        
        print("droite")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        p.ChangeDutyCycle(50)
        sleep(0.4)
        p.ChangeDutyCycle(0)
        
        
        print("bas")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        q.ChangeDutyCycle(50)
        sleep(0.4)
        q.ChangeDutyCycle(0)
        
        
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        j.ChangeDutyCycle(50)
        sleep(0.2)
        j.ChangeDutyCycle(0)
        
        
        print("droite")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        p.ChangeDutyCycle(50)
        sleep(0.4)
        p.ChangeDutyCycle(0)
        
        
        print("haut")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        q.ChangeDutyCycle(100)
        sleep(0.6)
        q.ChangeDutyCycle(0)
        
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        j.ChangeDutyCycle(50)
        sleep(0.2)
        j.ChangeDutyCycle(0)
        
        
        x='z'
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")