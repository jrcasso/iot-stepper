from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    time.sleep(5)
    led.toggle()
