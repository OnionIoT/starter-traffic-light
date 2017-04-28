from time import sleep
import onionGpio

# define pins
GREEN_PIN   = 0
AMBER_PIN  = 1
RED_PIN     = 2

# define states
ON      = 1
OFF     = 0

# durations for each light
redTime     = 5
amberTime   = 3
greenTime   = 5

# instantiate gpio objects
red     = onionGpio.OnionGpio(RED_PIN)
amber   = onionGpio.OnionGpio(AMBER_PIN)
green   = onionGpio.OnionGpio(GREEN_PIN)

# initialize to inputs in case there is external current to the pins
red.setInputDirection()
amber.setInputDirection()
green.setInputDirection()

# initialize to output
red.setOutputDirection(ON)
amber.setOutputDirection(OFF)
green.setOutputDirection(OFF)

# functions for switching lights
def setSignal(color):
    if color == "red":
        red.setValue(ON)
        amber.setValue(OFF)
        green.setValue(OFF)
        print "Signal is now " + color
    elif color == "amber":
        red.setValue(OFF)
        amber.setValue(ON)
        green.setValue(OFF)
        print "Signal is now " + color
    elif color == "green":
        red.setValue(OFF)
        amber.setValue(OFF)
        green.setValue(ON)
        print "Signal is now " + color
    else:
        print "Invalid color"
    
    return

# main loop
while True:
    # first red
    setSignal("red")
    sleep(redTime)
    
    # then green
    setSignal("green")
    sleep(greenTime)
    
    # then amber
    setSignal("amber")
    sleep(amberTime)