import time
from Adafruit_8x8 import ColorEightbyEight

segment = ColorEightbyEight(address = 0x70)
iter = 1

while True:
    iter = iter + 1
    for x in range (0,8):
        for y in range (0,8):
            segment.setPixel(x,y,iter%4)
            time.sleep(0.001)
