y = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
for i in y :
    print(i)
x = 2
while x < 1000:
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0 or x % 13 == 0 or x % 17 == 0 or x % 19 == 0 or x % 23 == 0 or x % 29 == 0 or x % 31 == 0:
        x += 1
    else:
        print(x)
        x += 1



