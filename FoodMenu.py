from random import *

adj1 = ["delicious", "scrumptious", "delectable", "organic", "sweet", "sour", "salty", "juicy", "gourmet", "flavorsome"]
adj2 = ["marinated", "glazed", "tasty", "fried", "soft", "seasoned", "savory", "creamy", "toasted", "smoked"]
food = ["chicken", "steak", "pancakes", "pasta", "salad", "salmon", "burrito", "noodles", "tuna", "croissant"]



for i in range(len(adj1)):
    i = i + 1
    list1 = randrange(0, len(adj1)) #list 1 = random number from length of list(adj1)
    list2 = randrange(0, len(adj2)) #list 2 = random number from length of list(adj2)
    listfood = randrange(0, len(food)) #listfood = random number from length of list(food)
    print (i,".", adj1[list1], adj2[list2], food[listfood]) #prints random word
    del(adj1[list1]) #deletes number from list(adj1)
    del(adj2[list2]) #deletes number from list(adj2)
    del(food[listfood]) #deletes number from list(food)