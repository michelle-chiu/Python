from Myro import *

def drawSquare(side):
    for i in range(4):
        turnBy(-90)
        forward(0.5, side)



init("sim")
#Square with loops

penDown()


#draw this -->

drawSquare(1)
drawSquare(2)
drawSquare(3)
drawSquare(4)

#bonus
for i in range(5):
    drawSquare(i)