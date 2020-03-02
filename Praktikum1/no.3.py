def jumlahHurufVokal(x) :
    z = 0
    w = ("A","I","U","E","O","a","i","u","e","o")
    for i in x:
        if i in w:
            z += 1
    y = (len(x), z)
    print(y)

def jumlahHurufKonsonan(x) :
    z = 0
    w = ("A","I","U","E","O","a","i","u","e","o")
    for i in x:
        if i not in w:
            z += 1
    y = (len(x), z)
    print(y)

