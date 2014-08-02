from Myro import *

#load a picture
myPic = makePicture ( pickAFile() ) #set variable

#--
white = makeColor(255, 255, 255) #sets screen to white

#loops through all the pixels
for p in getPixels(myPic):
    setColor(p, white)

show(myPic)
#savePicture(myPic, "purpleMichelle.jpg") #saves in Calico folder

#returns color values for a pixel
getRed(p)
getGreen(p)
getBlue(p)

#x & y coordinates of pixel itself
getX(p)
getY(p)

#changing the color
#p is a pixel, 0 <-- n <-- 255
setRed(p, n)
setGreen(p, n)
setBlue(p, n)

#setting a color
taupe = makeColor(72, 60, 50)
setColor(p, taupe)