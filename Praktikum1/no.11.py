def apakahKabisat(x):
    if x % 100 == 0 :
        if x % 400 == 0 :
            return True
        else:
            return False
    elif x % 400 == 0 or x % 4 == 0 :
        return True
    else:
        return False

