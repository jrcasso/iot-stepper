from machine import Pin, Timer
import utime
 
led_pin = Pin("LED", Pin.OUT)
dir_pin = Pin("GPIO0", Pin.OUT)
step_pin = Pin("GPIO1", Pin.OUT)
steps_per_revolution = 200
 
# Initialize timer
tim = Timer()
 
def step(t):
  global step_pin
  step_pin.value(not step_pin.value())
 
def rotate_motor(delay):
  # Set up timer for stepping
  tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)
 
def loop():
  counter = 0
  while True:
    print(f"Moving {counter}")
    led_pin.value(1)
    # Set motor direction clockwise
    dir_pin.value(1)

    # Spin motor slowly
    rotate_motor(2000)
    utime.sleep_ms(steps_per_revolution)
    tim.deinit()  # stop the timer
    utime.sleep(1)

    # Set motor direction counterclockwise
    dir_pin.value(0)

    # Spin motor quickly
    rotate_motor(1000)
    utime.sleep_ms(steps_per_revolution)
    tim.deinit()  # stop the timer
    led_pin.value(0)
    utime.sleep(1)

    counter += 1
 
if __name__ == '__main__':
    loop()

# from machine import Pin
# import utime

# led = Pin("LED", Pin.OUT)

# def flicker(count):
#   for i in range(count):
#     led.on()
#     utime.sleep_ms(100)
#     led.off()
#     utime.sleep_ms(100)
 
 
# class Stepper:
#   def __init__(self, step_pin, dir_pin):
#     self.step_pin = Pin(step_pin, Pin.OUT)
#     self.dir_pin = Pin(dir_pin, Pin.OUT)
#     self.position = 0
 
#   def set_speed(self, speed):
#       self.delay = 1 / abs(speed)  # delay in seconds

#   def set_direction(self, direction):
#       self.dir_pin.value(direction)

#   def move_to(self, position):
#       self.set_direction(1 if position > self.position else 0)
#       while self.position != position:
#         self.step_pin.value(1)
#         utime.sleep(self.delay)
#         self.step_pin.value(0)
#         self.position += 1 if position > self.position else -1

#   def move_forward(self, steps):
#       # self.set_direction(1 if position > self.position else 0)
#       # while self.position != position:
#       position = 0
#       while position < steps:
#         self.step_pin.value(1)
#         utime.sleep(self.delay)
#         self.step_pin.value(0)
#         if (position % 10 == 0):
#             print(f"Moved {position} steps")
#         position += 1
#         utime.sleep(self.delay)

# # Define the pins
# step_pin = Pin(17, Pin.OUT)
# dir_pin = Pin(16, Pin.OUT)

# # # Initialize stepper
# stepper = Stepper(step_pin, dir_pin)
 
# def loop():
#   try:
#     counter = 0
#     while True:
#       flicker(2)
#       # Move forward 2 revolutions (400 steps) at 200 steps/sec
#       print(f"{counter}: Moving")
#       stepper.set_speed(200)
#       stepper.move_forward(50)
#       counter += 1
#       utime.sleep(1)
#   except KeyboardInterrupt:
#     print("Program cancelled.")

# if __name__ == '__main__':
#   loop()
