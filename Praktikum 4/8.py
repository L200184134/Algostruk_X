import random

z = random.randint(0,1001)

print("Permainan tebak angka")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak!")

x = 1
y = input("Masukkan tebakan ke-" + str(x) + " --> ")
w = int(y)
while  w != z:
    if z in range(101):
        if w > z :
            print("Itu terlalu besar. Coba lagi!")
        if w < z :
            print("Itu terlalu kecil. Coba Lagi!")
        x += 1
        y = input("Masukkan tebakan ke -" + str(x) + " -->")
        w = int(y)
        if x == 7:
            raise AssertionError("Kesempatan anda telah habis")
    if z in range(101, 1001):
        if w > z :
            print("Itu terlalu besar. Coba lagi!")
        if w < z :
            print("Itu terlalu kecil. Coba Lagi!")
        x += 1
        y = input("Masukkan tebakan ke -" + str(x) + " -->")
        w = int(y)
        if x == 10:
            raise AssertionError("Kesempatan anda telah habis")
print("Ya. Anda benar!")
