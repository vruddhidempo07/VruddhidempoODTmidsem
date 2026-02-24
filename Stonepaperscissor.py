from machine import Pin, PWM
import time
import neopixel
import random

pb_1 = Pin(4,Pin.IN,Pin.PULL_UP)
pb_2 = Pin(33,Pin.IN,Pin.PULL_UP)
pb_3 = Pin(25,Pin.IN,Pin.PULL_UP)

neo = neopixel.NeoPixel(Pin(14),16)
buzz = Pin(18,Pin.OUT)

stone1_led = Pin(15,Pin.OUT)
paper1_led = Pin(21,Pin.OUT)
scissor1_led = Pin(12,Pin.OUT)

stone2_led = Pin(19,Pin.OUT)
paper2_led = Pin(22,Pin.OUT)
scissor2_led = Pin(26,Pin.OUT)

move=["stone","paper","scissors"]
leds_comp=[stone2_led,paper2_led,scissor2_led]
    
def calculate(x,y):
    if (x=="stone" and y=="scissors") or (x=="paper" and y=="stone") or (x=="scissors" and y=="paper"):
        print("You WIN!!!!!")        
        for i in range(2):         
            for j in range(16):
                neo[j]=(0,150,100)
                neo.write()
            time.sleep(0.2)
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.05)
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.05)
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.05)
            buzz.value(1)
            time.sleep(0.4)
            buzz.value(0)
            time.sleep(0.05)
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.5)
            buzz.value(0)

            for j in range(16):
                neo[j]=(0,0,0)
                neo.write()
            time.sleep(0.2)
            
    elif (x=="stone" and y=="paper") or (x=="paper" and y=="scissors") or (x=="scissors" and y=="stone"):
        print("Computer WINS!!!!!")
        for n in range(2):
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.2)
        for i in range(4):
            for j in range(16):
                neo[j]=(100,0,0)
                neo.write()
            time.sleep(0.2)
            for j in range(16):
                neo[j]=(0,0,0)
                neo.write()
            time.sleep(0.2)
   
    elif x==y:
        print("You TIED!")
        for n in range(2):
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
        for i in range(4):
            for j in range(16):
                neo[j]=(255,100,0)
                neo.write()
            time.sleep(0.2)
            for j in range(16):
                neo[j]=(0,0,0)
                neo.write()
            time.sleep(0.2)

def timer():
    buzz.value(1)
    time.sleep(0.5)
    buzz.value(0)
    print("stone")
    time.sleep(0.2)
    buzz.value(1)
    time.sleep(0.25)
    buzz.value(0)
    time.sleep(0.05)
    buzz.value(1)
    time.sleep(0.25)
    buzz.value(0)
    print("paper")
    time.sleep(0.2)
    buzz.value(1)
    time.sleep(0.1)
    buzz.value(0)
    time.sleep(0.05)
    buzz.value(1)
    time.sleep(0.3)
    print("scissors")
    buzz.value(0)
    print("GO!!!!!")
    
while True:
    if pb_1.value()==0 or pb_2.value()==0 or pb_3.value()==0:
        timer()
        if pb_1.value()==0:
            user="stone"
            stone1_led.value(1)
            r=random.randint(0,2)
            comp=move[]
            leds_comp[r].value(1)
            time.sleep(0.5)
            stone1_led.value(0)
            leds_comp[r].value(0)         
            calculate(user,comp)

        elif pb_2.value()==0:
            user="paper"
            paper1_led.value(1)
            r=random.randint(0,2)
            comp=move[r]
            leds_comp[r].value(1)
            time.sleep(0.5)
            paper1_led.value(0)
            leds_comp[r].value(0)           
            calculate(user,comp)
            
        elif pb_3.value()==0:
             user="scissors"
            scissor1_led.value(1)
            r=random.randint(0,2)
            comp=move[r]
            leds_comp[r].value(1)
            time.sleep(0.5)
            scissor1_led.value(0)
            leds_comp[r].value(0)        
            calculate(user,comp)
