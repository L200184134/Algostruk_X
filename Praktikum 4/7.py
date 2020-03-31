Daftar = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 14]

def binSe(kumpulan, target):
    a = []
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            a.append(mid)
            savepoint = mid
            while kumpulan[savepoint-1] == target:
                savepoint -= 1
                a.append(savepoint)
            savepoint1 = mid
            while kumpulan[savepoint1+1] == target:
                savepoint1 += 1
                a.append(savepoint1)
            a.sort()
            return a
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
