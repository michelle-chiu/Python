from Myro import *
from random import *

# Width and height of the simulator room, in pixels
roomWidth = 640
roomHeight = 480

# Parameters are: name of room, width, height, floor color
sim = Simulation("Empty Room", roomWidth, roomHeight, Color("green"))

# Top wall
sim.addWall((10, 10), (roomWidth-10, 20), Color("brown"))
# Bottom wall
sim.addWall((10, roomHeight-20), (roomWidth-10, roomHeight-10), Color("brown"))
# Left wall
sim.addWall((10, 10), (20, roomHeight-10), Color("brown"))
# Right wall
sim.addWall((roomWidth-20, 10), (roomWidth-10, roomHeight-10), Color("brown"))

sim.setup()
makeRobot("SimScribbler", sim)
setForwardness("scribbler-forward")

# Start your code below

while True:
    motors(1,1)
    if getStall() == 1:
        wait(2)
        backward(1,1)
        turnBy(randrange(90,270))