# Conditionals

if 5 < 4: #if True, if False
    print("of course")
    print("this is")
    print("true")
else:
    print("nothing makes sense")

x = 17
# "is x between 15 and 20?"
if x > 15 and x < 20:
    print("yes")
else:
    print("no") # if 20 > x > 15 doesn't work

# "is x not between 15 and 20?"
if x < 15 or x > 20:
    print(":)")
else:
    print(":(")