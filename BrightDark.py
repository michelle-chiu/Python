from Myro import *
from random import *


myPic = makePicture( pickAFile() )
show(myPic)
for p in getPixels(myPic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)

    #brighter
    setRed(p, r + randrange(100,150))
    setGreen(p, g + randrange(100,150))
    setBlue(p, b + randrange(100,150))

    #darker
    setRed(p, r - randrange(100,150))
    setGreen(p, g - randrange(100,150))
    setBlue(p, b - randrange(100,150))

show(myPic)