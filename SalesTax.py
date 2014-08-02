#Write a function to calculate sales tax.

def salestax(price):
    tax = price * 0.087
    return tax

t = salestax(25.00)
total = 25.00 + t
print("Total price:", total)