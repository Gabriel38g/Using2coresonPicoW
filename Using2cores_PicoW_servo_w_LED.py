from machine import Pin
import SERVO # --> don't forget to include SERVO.py available on this project folder 
import time
import  _thread

greenPin = 14
redPin = 15

redLED = Pin(redPin,  Pin.OUT)
greenLED = Pin(greenPin,  Pin.OUT)

redOn=.5
redOff=.5

greenOn=.2
greenOff=.2

greenBlink=10
redBlink=3

# homework settings
servoPin=16
blueServo=SERVO.servo(servoPin)
greenpos=45
redpos=120
jobdone = "R"

def othredBlinker(redOn,  redOff):
    global jobdone
    x=0
    while x < redBlink:
        redLED.value(1)
        time.sleep(redOn)
        redLED.value(0)
        time.sleep(redOff)
        x = x + 1
    jobdone = "G"
    _thread.exit()
    
def othgreenBlinker(gOn,  gOff):
    global jobdone
    x = 0
    #blueServo.pos(greenpos)
    while x < greenBlink:
        greenLED.value(1)
        time.sleep(gOn)
        greenLED.value(0)
        time.sleep(gOff)
        x = x + 1
    jobdone = "R"
    _thread.exit()
    
while True:
    
    if jobdone == "R":
        p = greenpos
        _thread.start_new_thread(othredBlinker,  [redOn, redOff])
        while p <= redpos:
            blueServo.pos(p)
            p = p+1
            time.sleep(.08)
            
    
    if jobdone == "G":
        p = redpos
        _thread.start_new_thread(othgreenBlinker,  [greenOn, greenOff])
        while p >= greenpos:
            blueServo.pos(p)
            p = p -1
            time.sleep(.08)
            
    #time.sleep(1)

