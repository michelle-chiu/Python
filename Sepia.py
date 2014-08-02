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
    if grayValue > 100: #ObamaYellow
        setRed(p,112)
        setGreen(p,66)
        setBlue(p,20)


show(myPic)