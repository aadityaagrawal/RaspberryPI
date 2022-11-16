import RPi.GPIO as GPIO 
from time import sleep

trig_pin = 18
echo_pin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(tring_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)

def send_signal():
    GPIO.output(trig_pin, True)
    sleep(0.00001)
    GPIO.output(trig_pin, False)

def receive_signal (timeout, value):
    count = timeout
    while(GPIO.input(echo_pin) != value and count>0):
        count = count - 1

def distance ():
    send_signal()
    receive_signal(10000, True)
    start = time.time()
    receive_signal(10000, False)
    finish = time.time()
    pulse_length = finish-start
    
    distance_in_cms = pulse_length/0.000058
    distance_in_inches = distance_in_cms/2.5
    return (distance_in_cms,distance_in_inches)

while True :
    print (distance())
    sleep(1)


