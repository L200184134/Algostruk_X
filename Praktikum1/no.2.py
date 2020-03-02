def Square(x,y) :
    z = 0
    while z < x :
        if z == 0 or z == x-1:
            print("@" * y)
        elif z != 0 and z != x :
            print("@" + " " * 3 + "@")
        z += 1
