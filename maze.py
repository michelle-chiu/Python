import Myro
from Myro import *
from Graphics import *
from random import *
sim = Simulation("Maze World", 500, 500, Color("green"))

#light
sim.addLight((190, 450), 25, Color("yellow"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("brown"))
sim.addWall((10, 10), (20, 490), Color("brown"))
sim.addWall((480, 10), (490, 490), Color("brown"))
sim.addWall((10, 480), (490, 490), Color("brown"))

#inner maze
sim.addWall((150, 300), (380, 310), Color("brown"))
sim.addWall((150, 180), (380, 210), Color("brown"))
sim.addWall((380, 180), (390, 310), Color("brown"))
sim.addWall((150, 300), (160, 490), Color("brown"))
#sim.addWall((150, 10), (160, 100), Color("brown"))
#sim.addWall((150, 80), (390, 100), Color("brown"))

#begin simulation
sim.setup()
makeRobot("SimScribbler", sim)
setForwardness("scribbler-forward")

#STUDENTS! Write your code here to solve the maze

while True:
    motors(0.5,0.5)
    if getIR("left") == 0:
        wait(0.2)
        backward(0.5,1)
        turnBy(randrange(30,50))
    if getIR("right") == 0:
        wait(0.2)
        backward(0.5,1)
        turnBy(randrange(-50,-30))
    if getIR("left") and getIR("right") == 0:
        wait(0.2)
        backward(0.5,1)
        turnBy(randrange(0,30))
    if getStall() == 1:
        wait(0.2)
        backward(0.5,1)
        turnBy(randrange(30,55))
    if getLight("center") < 100:
        motors(0,0)