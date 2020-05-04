class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data, priority):
        entry = PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong" 
        max = 0
        for i in range(len(self.qlist)): 
            if self.qlist[i].priority < self.qlist[max].priority: 
                max = i 
        hasil = self.qlist[max] 
        del self.qlist[max] 
        print(hasil.item)

class PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

S = PriorityQueue()

S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)
S.dequeue()
S.dequeue()
S.dequeue()
