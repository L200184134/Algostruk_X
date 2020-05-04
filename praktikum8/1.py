class Stack(object):
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.item)
    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.item[-1]
    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.item.pop()
    def push(self, data):
        self.item.append(data)
        
def cetakHexa(a):
    b = Stack()
    if a == 0:
        b.push(0)
    while a != 0:
        c = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        sisa = a % 16
        if sisa in c:
            sisa = c[sisa]
        a = a // 16
        b.push(sisa)
    hasil = ""
    for i in range(len(b)):
        hasil += str(b.pop())
    return hasil
        
