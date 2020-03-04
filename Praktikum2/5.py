class Mahasiswa(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.t = []
    def str(self):
        s = self.nama + ", NIM " + str(self.NIM)\
            + ", Kota "+self.kotaTinggal\
            + ", Uang Saku Rp. "+str(self.uangSaku)\
            + " tiap Bulan."
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, i):
        print("Saya baru saja makan", i, " sambil belajar")
        self.keadaan = 'Kenyang'
        
    def ambilKotaTinggal(self):
        return self.kotaTinggal
        
    def perbaruiKotaTinggal(self,j):
        self.j = j
        self.kotaTinggal = self.j
          
    def tambahUangSaku(self,c):
        
        self.uangSaku = self.uangSaku + c
        
    def ambilKuliah(self,z):
        self.t.append(z)
        
    def listKuliah(self):
        return self.t
        
    def menghapusKuliah(self,h):
        self.t.remove(h)