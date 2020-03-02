def faktorPrima(x) :
    y = 0
    w = 0
    v = 0
    u = 0
    t = 0
    z = []
    while x % 2 == 0 :
        x = x / 2
        z.append(2)
    while x % 3 == 0 :
        x = x / 3
        z.append(3)
    while x % 5 == 0 :
        x = x / 5
        z.append(5)
    while x % 7 == 0 :
        x = x / 7
        z.append(7)
    z.append(int(x))
    if 1 in z :
        z.remove(1)  
    print(tuple(z))

