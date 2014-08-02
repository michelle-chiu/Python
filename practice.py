#1
def spam():
    print("Eggs!")

spam()

#2
def welcome(name):
    print("Welcome", name)

welcome("Alice")
welcome("Beth")
welcome("Carla")

#3
def tip(cost):
    tip = cost * .15
    print("You owe:", tip)

tip(13)

#4
def tip2(cost):
    tip2 = cost * .15
    return tip2


bill = 13.00
gratituity = tip2(bill)
print("You owe:", gratituity)

#5
def ctof(temp):
    ft = ((9/5) * temp) + 32
    return ft

boiling = ctof(100)
freezing = ctof(0)
print(boiling)
print(freezing)


#6
def spam(n):
    for i in range(n):
        print("Eggs!")

spam(100)

#7
def sumOf(n):
    total=0
    for i in range(n+1):
        total = total + i
    return total

print(sumOf(100))
print(sumOf(1000))


#8
def factorial(n):
    if n==0: #bonus
        return 1
    else:
        value = 0
        for i in range(n+1):
            if i == 0:
                value = 1
            else:
                value = value * i
        return value




a = factorial(0)
b = factorial(10)
c = factorial(16)
print(a, b, c)
