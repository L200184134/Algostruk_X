class Manusia():
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Assalamu'alaikum")
    def makan(self,s):
        print("saya baru saja makan "+s)
    def olahraga(self,k):
        print("saya baru saja olahraga "+ k)
    def mengalikanDenganDua(self,n):
        return n*2

class siswaSMA(Manusia):
    def __init__(self,nama):
        self.nama = nama
        print("Assalamu'alaikum "+self.nama)

    def apaYangDisukai(self,p):
        print("Saya suka "+p)