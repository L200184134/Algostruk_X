x = 1
while x < 101 :
    if x % 3 == 0 and x % 5 == 0 :
        print("Python UMS")
    elif x % 5 == 0 :
        print("UMS")
    elif x % 3 == 0 :
        print("Python")
    else:
        print(x)
    x += 1

