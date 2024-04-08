from machine import Pin, Timer
import utime
 
led_pin = Pin("LED", Pin.OUT)
enable_pin = Pin("GPIO12", Pin.OUT)
enable_switch_pin = Pin("GPIO13", Pin.IN)
dir_pin = Pin("GPIO14", Pin.OUT)
step_pin = Pin("GPIO15", Pin.OUT)
steps_per_revolution = 200
 
# Initialize timer
tim = Timer()
 
def step(t):
  global step_pin
  step_pin.value(not step_pin.value())

def check_for_active_toggle():
  print(f"enable_switch {enable_switch_pin.value()}")
  if enable_switch_pin.value() == 1:
    print("Changing enablement state")
    enable_pin.value(not enable_pin.value())
    utime.sleep(1)
  print(f"enable {enable_pin.value()}")


def enabled():
  print(f"enabled? {enable_pin.value()}")
  return not enable_pin.value()

def rotate_motor(delay):
  # Set up timer for stepping
  frequency = 1000000.0/delay
  print(f"Sending pulses every {1.0/frequency} seconds...")
  tim.init(freq=frequency, mode=Timer.PERIODIC, callback=step)

def rotate_with_speed(steps_per_second):
  # In steps per second, e.g.:
  # 20 steps / s * rev / 200 step = 0.1 revs / s = 1/10 hz
  frequency = steps_per_second * (1.0 / 200.0)
  print(f"Sending pulses every {1.0/frequency} seconds...")
  tim.init(freq=frequency, mode=Timer.PERIODIC, callback=step)

def loop():
  counter = 0
  enable_pin.value(1)
  dir_pin.value(1)
  spin = float(input("Enter the rotation step delay: "))

  while True:
    check_for_active_toggle()
    if enabled():
      if counter != 0: tim.deinit()
      led_pin.value(1)
      # Spin motor quickly
      # rotate_motor(1000)
      rotate_motor(spin or 800.0)
      # utime.sleep_ms(steps_per_revolution)
      # tim.deinit()  # stop the timer
      led_pin.value(0)
      utime.sleep(1)

      counter += 1
    else:
      tim.deinit()
      step_pin.value(0)
      counter = 0
      utime.sleep(1)
 
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
