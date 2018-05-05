# Metro IO demo
# Welcome to CircuitPython 2.2.0 :)

import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import audioio
import touchio
import simpleio


# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Digital input with pullup on D2, D3, D4, D5, D6
buttons = []
for p in [board.D2, board.D3, board.D4, board.D5, board.D6]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)


# Digital output  on D8, D9, D10, D11, D12
buttonLeds = []
for p in [board.D8, board.D9, board.D10, board.D11, board.D12]:
    led = DigitalInOut(p)
    led.direction = Direction.OUTPUT
    buttonLeds.append(led)

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

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  for led in buttonLeds:
    if i < 125:
      led.value = True
    else:
      led.Value = False

  if not buttons[0].value:
      print("Button D2 pressed!", end ="\t")

  if not buttons[1].value:
      print("Button D3 pressed!", end ="\t")

  if not buttons[2].value:
      print("Button D4 pressed!", end ="\t")
  
  if not buttons[3].value:
      print("Button D5 pressed!", end ="\t")

  if not buttons[4].value:
      print("Button D6 pressed!", end ="\t")


  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down

  print("")
