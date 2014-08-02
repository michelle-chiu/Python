from Myro import *


myPic = makePicture( pickAFile() )

show(myPic)

for p in getPixels(myPic):
    #get red, green, and blue
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)

    #figure out how "bright" the color is
    grayValue = (r + g + b)/3

    #set according to conditionals
    if grayValue > 180: #ObamaYellow
        setRed(p,252)
        setGreen(p,227)
        setBlue(p,166)
    elif grayValue > 120: #ObamaBlue
        setRed(p,112)
        setGreen(p,150)
        setBlue(p,158)
    elif grayValue > 60: #ObamaRed
        setRed(p,217)
        setGreen(p,26)
        setBlue(p,33)
    else:                #ObamaDarkBlue
        setRed(p,0)
        setGreen(p,51)
        setBlue(p,76)


show(myPic)