class Mahasiswa():
    def __init__(self,nama,NIM,Kota,us):
        self.nama = nama
        self.NIM = NIM
        self.Kota = Kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama \
            + " NIM : "+str(self.NIM)\
            + " Kota : "+self.Kota\
            + " Uang Saku : "+self.uangSaku+" perbulan"
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilTempatTinggal(self):
        return self.Kota
    def perbaruiTempatTinggal(self,e):
        self.Kota = e
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,f):
        self.uangSaku = self.uangSaku + f
a = input("Nama : ")
b = input("NIM : ")
c = input("Kota : ")
d = input("Uang Saku = ")
x = Mahasiswa(a, b, c, d)
print(x)