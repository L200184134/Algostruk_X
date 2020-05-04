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

nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
print(nilai.item)
