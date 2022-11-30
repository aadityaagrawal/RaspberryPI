import RPi.GPIO as GPIO 
from time import sleep

coil_A1 = 22
coil_A2 = 24
coil_B1 = 26
coil_B2 = 28

GPIO.setmode(GPIO.BOARD)
GPIO.setup(coil_A1, GPIO.OUT)
GPIO.setup(coil_B1, GPIO.OUT)
GPIO.setup(coil_A2, GPIO.OUT)
GPIO.setup(coil_B2, GPIO.OUT)

forward = ['1010','0110','0101','1001']
backward = ['1001','0101','0110','1010']

def set_step (step):
    GPIO.output(coil_A1, step[0]=='1')
    GPIO.output(coil_A2, step[1]=='1')
    GPIO.output(coil_B1, step[2]=='1')
    GPIO.output(coil_B2, step[3]=='1')

def forw (delay,steps):
    for i in range(steps):
        for step in forward:
            print(step)
            set_step(step)
            sleep(delay)

def back (delay,steps):
    for i in range(steps):
        for step in backward:
            print(step)
            set_step(step)
            sleep(delay)

while True :
    choice = input ("Enter CHOICE F/B/S: ")
    if (choice == "F"):
        set_step("0000")
        forw(1,2)
        set_step("0000")
        sleep(2)

    if (choice == "B"):
        set_step("0000")
        back(1,2)
        set_step("0000")
        sleep(2)

    if (choice == "S"):
        print("Stopping")
        break

