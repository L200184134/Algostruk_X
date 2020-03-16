m1 = [[2, 3], [4, 5]]
m2 = [[10, 20], [5, 6]]


# Numero 1a
def Memastikan(matrix):
    """ensure Integer data type by using"""
    for x in matrix:
        for i in x:
            assert isinstance(i, int), "Must Integer"
        return ("Matrix is Consistent")

# Numero 1b
def Ukuran(matrix):
    """Take the size of the matrix"""
    return ("Matrix size = " + str(len(matrix)) + " x " + str(len(matrix[0])))

# Numero 1c
def Jumlah(matrix1, matrix2):
    """sum of 2 Matrix"""
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            for y in range(0, len(matrix1[0])):
                print(matrix1[x][y] + matrix2[x][y], end=' '),
            print()
    else:
        print("Inappropriate Matrix")

# Numero 1d
def Kali(matrix1, matrix2):
    """multiplication of 2 Matrix"""
    mat3 = []
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            row = []
            for y in range(0, len(matrix1[0])):
                total = 0
                for z in range(0, len(matrix1)):
                    total = total + (matrix1[x][z] * matrix2[z][y])
                row.append(total)
            mat3.append(row)

        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end=' ')
            print()
    else:
        print("Inappropriate Matrix")

# Numero 1d
def determinan(matrix):
    """Calculate the determinant of Matrix"""
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total - total2)
        return ""
    else:
        print("Matrix Type Must in 'Square Matrix' ")


# Main Method
print(Memastikan(m1))
print(Ukuran(m1))
Jumlah(m1, m2)
Kali(m1, m2)
print(determinan(m1))

# Numero 2
# Numero 2a
def BuatNol(m, n):
    """m for row, n for coloumn"""
    matriks = [[0 for j in range(m)] for i in range(n)]
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",m,'x',n)

def buatNol(m):
    """m for coloumn and it is square matrix same ordo"""
    matriks = [[0 for j in range(m)] for i in range(m)]
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",m,'x',m)


# Numero 2b
def buatIdentitas(m):
    """Identity Matrix"""
    matriks = [[1 if j == i else 0 for j in range(m)] for i in range(m)]
    for i in matriks:
        print (i)
    print ("Matriks identitas ber ordo",m,'x',m)

buatNol(4)
BuatNol(3,2)
buatIdentitas(4)


# Numero 3
class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def cetak(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode

    def cari(head, cari):
        curr = head
        while curr != None:
            if curr.data == cari:
                print("Data ditemukan!")
            else:
                print("Check data!")
            curr = curr.nextNode

    def tambahDepan(head):
        newNode = Node(1)
        newNode.nextNode = head
        head = newNode
        return head

    def tambahAkhir(head):
        curr = head
        while curr is not None:
            if curr.nextNode == None:
                newNode = Node(25)
                curr.nextNode = newNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr

    def tambah(head, posisi):
        newNode = Node(8)
        newNode.nextNode = posisi.nextNode
        posisi.nextNode = newNode
        head.head = posisi
        return head

    def hapus(head, posisi):
        curr = head
        while curr != None:
            if curr.nextNode.data == posisi:
                curr.nextNode = curr.nextNode.nextNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr


a = Node(14)
b = Node(76)
c = Node(54)
d = Node(9796)

a.nextNode = b
b.nextNode = c
c.nextNode = d
# print(a.nextNode.nextNode.data)
a.tambah(b)
a.cari(14)
a.tambahAkhir()
a.tambahDepan()
a.cetak()

# coba = Node(1)
# coba.tambah(b)
# coba.cetak()

class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak():
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head

    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr

hell = doubly_linked(14)
heaven = doubly_linked(15124)
between = doubly_linked(9999)
hell.Next = heaven
heaven.Next = between
hell.simpulAwal()
hell.simpulAkhir()
between.mencetak()

# Collected by Donny L200183161
# Angel tenan to mas --" ajarin gooo

