#Lists: a variable that represents a group of things.

#create
fruits = ["oranges", "apples", "kiwis", "limes"]

#access
print(fruits[2])

#append/add
fruits.append("bananas")

#change
fruits[2] = "mangoes"

#delete
del(fruits[2])
#or
fruits.remove("apples")

#insert
fruits.insert(2, "peaches")

#remove
fruits.remove("oranges")

#find how many items in list
print(len(fruits))
#how many letters in word
print(len(fruits[2]))

#mutable: "can be changed"
#list: numbers = [1, 2, 8, 4]

#immutable: "cannot be changed"
#tuple: numbers 1, 2, 8, 4

#"Strings are words, phrases, sentences,
# Strings ARE lists (of letters).

word = abracadabra
if "b" in word:
    print("the word contains the letter b")
else:
    print("it doesn't have any b's")