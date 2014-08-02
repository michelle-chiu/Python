#Lessons from Rando-Platter
#Hard-coding VS Soft-coding

from random import *
fruits = ["apple", "banana", "lime"]

#this is hard-coding:
#if we make a change in one part of the program, this part will change as well.

print(fruits[randrange(0,4)]) #doesn't include last number

    #this is soft-coding:
print(fruits[randrange(0, len(fruits))])