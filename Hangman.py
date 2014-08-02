from random import *
from Myro import *
 
print ("Welcome to Hangman! The selection of words to guess are animal-themed.")
words = ["tiger", "walrus", "lynx", "hyena", "bison", "horse"]
 
guessword = words[randrange(0,6)] #guessword is the word they need to guess
#print (guessword)                #to check
length = len(guessword)           #length is how long the "guessword" is
print("This word has", length, "letters.")
 
 
while length != 0:
    letter = raw_input("Please guess a letter.")
    if letter in guessword:
        print("The word contains the letter", letter, ".")
        length = length - 1
    else:
        print("The word does not contain the letter", letter, ".", "Please try again.")
 
print("Congratulations, you've guessed the word", guessword, "!")