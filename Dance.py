from Myro import *

init("sim")

#Dance: wiggle rockstep wiggle wiggle rockstep

#Defines the function wiggle.
#This packages all the instruction together.
#It DOES NOT perform the instructions.
def wiggle():
    turnBy(15)
    turnBy(-30)
    turnBy(15)
#Defines the function rockstep.
def rockstep():
    forward(1, 0.25)
    backward(1, 0.5)
    forward(1, 0.25)

wiggle()
rockstep()
wiggle()
wiggle()
rockstep()
