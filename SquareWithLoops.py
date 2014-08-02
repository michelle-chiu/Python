from Myro import *

def drawSquare(side):
    for i in range(4):
        turnBy(-90)
        forward(1, side)



init("sim")
#Square with loops

penDown()
for i in range(4):
    forward(1,4)
    turnBy(-90)
for i in range (4):
    forward(1,3)
    turnBy(-90)
for i in range(4):
    forward(1,2)
    turnBy(-90)
for i in range(4):
    forward(1,1)
    turnBy(-90)

#draw this -->

drawSquare(4)
drawSquare(3)
drawSquare(2)
drawSquare(1)