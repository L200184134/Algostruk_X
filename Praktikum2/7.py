class Manusia():
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Assalamu'alaikum "+self.nama)
    def makan(self):
        print("saya baru saja makan ")
    def olahraga(self,k):
        print("saya sudah melakukan olahraga "+ k)
    def mengalikanDenganDua(self,n):
        return n*2
class Mahasiswa(Manusia):
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
        self.keadaan = "Kenyang"
        print("Saya makan", i, " sambil belajar, oleh sebab itu saya "+self.keadaan)
                
    def ambilKotaTinggal(self):
        return self.kotaTinggal
        
    
class mhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")
y = mhsTIF("Mahardhika","L200184134","Purwakarta",300000)
y.ucapkanSalam()##fromclassManusia
y.olahraga("lari")##fromclassManusia
y.makan("Gado-gado")##fromclassMahasiswa
y.ambilNama()##fromclassMahasiswa
y.ambilNIM()##fromclassMahasiswa
y.ambilKotaTinggal()##fromclassMahasiswa
y.ambilUangSaku()##fromclassMahasiswa
y.katakanPy()##fromclassmhsTIF
