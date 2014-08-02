from Myro import *
from random import *

GWC = ["Michelle P.", "T'Yanni", "Vicky", "Ava", "Danielle", "Michelle C.", "Shelly",
 "Ashley", "Meredith", "Kelsey", "Danasiah", "Aysha", "Demeara", "Amarissa", "Francesca", "Yennifer",
  "Tolu", "Luisa", "Katrina"]
#choose 1 student
print (GWC[randrange(0,19)])
#make groups
for i in range(19):
    i = i + 1
    list1 = randrange(0, len(GWC))
    print (i,".", GWC[list1])
    del(GWC[list1])

#with inputted names
raw_input
