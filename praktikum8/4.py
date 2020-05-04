class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def getFrontMost(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        print(self.qlist[0])
    def getRearMost(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        print(self.qlist[-1])
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        print(self.qlist.pop())
    def enqueue(self, data):
        self.qlist.append(data)

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def getFrontMost(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        print(self.qlist[0])
    def getRearMost(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        print(self.qlist[-1])
    def enqueue(self, data, priority):
        entry = PriorityQEntry(data, priority)
        self.qlist.append(entry.item)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)

class PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        

Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)
Q.enqueue(7)
print(Q.qlist)
Q.getFrontMost()
Q.getRearMost()

print("")

S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)
print(S.qlist)
S.getFrontMost()
S.getRearMost()
