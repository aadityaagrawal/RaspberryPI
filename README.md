# RaspberryPI

This Repository contain the code of all the programs which i learned during RaspberryPI lectures.


### DS18B20:

1. It is digital temperature reading sensor.
2. The best thing about DS18B20 is data is transfer through one wire.
3. They have unique 32-bit addressing system which allow us to connect multiple DB18S20 sensor together.
4. The RaspberryPi don't have a ADC chip. The DS18B20 sensor convert the analog signal to digital on the way. Therefore unlike TMP36 sensor we can get digital sensor.
5. It can operate in the range of -55 C to 125 C.

### SR04:

1. The SR-04 is a fun distance measuring sensor it is used to find the distance of the object or to detect the presence of any object etc.
2. It can measure distance from 2 cm upto 400 cm with an accuracy of 0.5 micrometer.
3. It have 4 pins vout, trig, echo and ground.
4. vout is used for voltage transfer, trig is used to transmit ultrasonic waves, echo is used to receive reflected ultrasonic sound waves.

#### Working of SR-04 :
Trig require 5V for 10 microsecond to generate ultrasonic waves and generate 8 ultrasonic waves. When the waves strikes an object it reflect back the ultrasonic waves which was received by echo that measure how long it ultrasonic waves take to return back. It then sends all the information to the micro controller which divides the time by 2 and multiple it the speed of ultrasonic sound wave to calculate how far the object is from the sensor. 
 

### CherryPy :

CherryPy is an open source library which we can use to create instant web page. Infact it is one of the oldest library avaliable in python for web development. It is not that much popular because it don't have seperate code for front end and back end unlike modern language like mongoDB, flask etc.

By using CherryPy one can create a static web page rapidly without coding much and save their time.
