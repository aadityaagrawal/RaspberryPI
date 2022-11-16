import Adafruit_DHT

dht11_sensor = Adafruit_DHT.DHT11
pin = 19

humidity, temperature = Adafruit_DHT.read_retry(dht11_sensor,pin)

print (f"The humidity is {} and the temperature is {}".format(humidity,temperature))

