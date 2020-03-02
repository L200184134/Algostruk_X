def rerata(b) :
    y = 1
    z = 0
    x = 0
    while y <= len(b) :
        x += b[z]
        y += 1
        z += 1
    return x/len(b)


