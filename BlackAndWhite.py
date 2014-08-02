from Myro import *
 
myPic = makePicture( pickAFile() )
 
for p in getPixels(myPic):
    #get red, green, and blue
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
 
    #figure out how "bright" the color is
    brightness = (r + g + b)/3
 
    #make and set the color
    gray = makeColor(brightness, brightness, brightness)
    setColor(p, gray)
 
show(myPic)