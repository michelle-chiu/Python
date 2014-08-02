from Myro import *

myPic = makePicture( pickAFile() )

show(myPic)

for p in getPixels(myPic):
    #get red, green, and blue
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)

    #set according to conditionals
    if r > 180:
        setRed(p,255)
    elif r > 120:
        setRed(p,112)
    elif r > 60:
        setRed(p,170)
    else:
        setRed(p,85)

    if g > 180:
        setGreen(p,255)
    elif g > 120:
        setGreen(p,112)
    elif g > 60:
        setGreen(p,170)
    else:
        setGreen(p,85)


    if b > 180:
        setBlue(p,255)
    elif b > 120:
        setBlue(p,112)
    elif b > 60:
        setBlue(p,170)
    else:
        setBlue(p,85)

show(myPic)