from Myro import *

init("sim")
def L():
    penDown()
    motors(0.17,0.5,3)
    motors(0.0000005,0.8,1)
    turnBy(-75)
    forward(1,0.5)
    turnBy(-50)
    forward(1,0.4)
    turnBy(-85)
    forward(1,3)
    motors(1,0.1,1.5)
    turnBy(75)
    forward(1,0.5)
    turnBy(75)
    forward(1,0.5)
    turnBy(71)
    forward(1,3)

L()