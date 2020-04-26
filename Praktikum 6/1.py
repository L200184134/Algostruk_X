class MhsTIF:
    def __init__(self, nama, nim, kota, uang):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang
    def __str__ (self) :
        s = self.nama + " " + str(self.nim) + " " + self.kota + " " + str(self.uang)
        return s
    def getNim(self) :
        return self.nim

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

def mergesort(A) :
    if len (A) > 1 :
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergesort(separuhkiri)
        mergesort(separuhkanan)

        i=0;j=0;k=0
        while i < len (separuhkiri)and j < len (separuhkanan) :
            if separuhkiri[i].nim < separuhkanan[j].nim :
                A[k].nim = separuhkiri[i].nim
                i = i+1
            else :
                A[k].nim = separuhkanan[j].nim
                j = j+1
            k = k+1

        while i < len (separuhkiri) :
            A[k].nim = separuhkiri[i].nim
            i = i+1
            k = k+1
        while j < len (separuhkanan) :
            A[k].nim = separuhkanan[j].nim
            j = j+1
            k = k+1

        return A
    
def quicksort(A):
    quicksortbantu (A,0, len(A) -1)
    return A

def quicksortbantu(A, awal, akhir):
    if awal < akhir :
        titikbelah = partisi(A, awal, akhir)
        quicksortbantu(A, awal, titikbelah -1)
        quicksortbantu(A, titikbelah +1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal].getNim()

    penandakiri = awal +1
    penandakanan = akhir

    selesai = False
    while not selesai :
        while penandakiri <= penandakanan and \
              A[penandakiri].getNim() <= nilaipivot :
            penandakiri +=1
        while A[penandakanan].getNim() >= nilaipivot and \
            penandakanan >= penandakiri :
            penandakanan -=1
        if penandakanan < penandakiri :
            selesai = True
        else :
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

      
mergesort(Daftar)
for i in Daftar:
    print(i)
print(" ")
quicksort(Daftar)
for i in Daftar:
    print(i)
