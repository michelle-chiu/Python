#1 and 2 produce the same results.
#0 and 3 produce the same results.

#0
for i in range(5):
    print(i)

fruits = ["apples", "oranges", "strawberries"]

#1
for f in fruits:
    print (f)
    #prints list of fruits

#2
for i in range( len(fruits) ):
    print(fruits[i])

#3
for i in range( len(fruits) ):
    print ( i )