class MhsTIF:
    def __init__(self, nama, nim, kota, uang):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
y = 0
for i in range(len(Daftar)-1):
    x = Daftar[y]
    for j in Daftar[y:]:
        if x.nim > j.nim:
            x = j
        else:
            continue
    Daftar.remove(x)
    Daftar.insert(y, x)
    y += 1
for i in Daftar:
    print(i.nim, end = " ")
    
