class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def kunjungi(self, curNode):
        self.head = curNode
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

a = Node(10)
b = Node(12)
c = Node(15)

a.next = b
b.next = c

print(a.data)
print(a.next.next.data)
print(a.kunjungi(a))
