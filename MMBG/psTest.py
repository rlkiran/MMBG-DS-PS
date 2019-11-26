import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

session = False
startPin = 4
stopPin = 17
count = 0
Level = 0

GPIO.setup(startPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stopPin, GPIO.IN, GPIO.PUD_UP)
# print("Session Automatically Starts on Drawing")
while True:
    startState = GPIO.input(startPin)
    stopState = GPIO.input(stopPin)
    if count >= 10 and session:
        session = False
        print("Level Down")
        if Level > 0:
            Level -= 1
        count = 0
    if (stopState == GPIO.LOW and count < 10):
        Level += 1
        print("Level Up ",Level)
        count = 0
        time.sleep(1)
    if(startState == GPIO.LOW):
        session = True
    if(session):
        if(startState == GPIO.HIGH):
            session = False
            count += 1
            time.sleep(0.5)
            print("Level ",Level," Miss count ",count)
        # print("COnnected")
        # time.sleep(1)
    #if(not session):
     # pass
      #  print("DIZCOnnected")
      #  time.sleep(1)
print("LEVEL DOWN")