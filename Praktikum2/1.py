###A
class Pesan(object) :
    def __init__(self,p):
        self.p = p
    def apakahTerkandung(self,s):
        if s in self.p :
            print("true")
        else:
            print("False")

###B
    def hitungKonsonan(self):
        e = 0
        d = {"Q","W","R","T","Y","P","S","D","F","G","J","K","L","M","N","B","V","C","X","Z",
             "q","w","r","t","y","p","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z"}
        for j in self.p :
            if j in d :
                e += 1
            else :
                continue
        return e
###C
    def hitungVokal(self):
        y = 0
        x = {"A","I","U","E","O","a","i","u","e","o"}
        for i in self.p :
            if i in x :
                y += 1
            else :
                continue
        return y