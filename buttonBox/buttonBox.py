# Metro IO demo
# Welcome to CircuitPython 2.2.0 :)

import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from pulseio import PWMOut
import audioio
import touchio
import simpleio
import random


# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# pizeo buzzer
buzzer = PWMOut(board.D7, variable_frequency=True)
buzzer.frequency = 262
OFF = 0
ON = 2**15

# Digital input with pullup on D2, D3, D4, D5, D6
buttons = []
for p in [board.D2, board.D3]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)


# Digital output  on D8, D9, D10, D11, D12
buttonLeds = []
for p in [board.D8, board.D9]:
    buttonLed = DigitalInOut(p)
    buttonLed.direction = Direction.OUTPUT
    buttonLeds.append(buttonLed)

######################### HELPERS ##############################


# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

    
######################### MAIN LOOP ##############################



# randomize the starting button
activeButtonId = random.randint(0,1)

i = 0
while True:
  # spin internal neopixel LED around for pretty lightssss
  dot[0] = wheel(i & 255)

  activeButton = buttons[activeButtonId]
  activeButtonLed = buttonLeds[activeButtonId]

  if i < 125:
    activeButtonLed.value = True
  else:
    activeButtonLed.value = False

  # if i < 125:
  #   buzzer.duty_cycle = ON
  # else:
  #   buzzer.duty_cycle = OFF

  if not activeButton.value:
    activeButtonId = random.randint(0,1)
    activeButtonLed.value = False
    time.sleep(1.2)

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down

  # print("")
