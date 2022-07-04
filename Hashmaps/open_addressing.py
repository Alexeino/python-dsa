# Linear Probing
class MyHash:

    def __init__(self,c):
        self.cap = c
        self.table = [-1] * c
        self.size = 0

    # [-1,-1,-1,-1,-1,-1,-1]
    def hash(self,key):
        return key % self.cap

    def insert(self,x):
        
        if self.size == self.cap:
            return False #Table full

        if self.search(x):
            return False # Element already present

        h = self.hash(x)
        i = h
        t = self.table
        
        if self.size == self.cap:
            return False 

        while t[i] not in (-1,-2):
            i = (i+1) % self.cap # so that i doesn't exceed the capacity
            #i += 1

        t[i] = x

        self.size += 1
        return True

            
    def search(self,x):   # x = 56
        h = self.hash(x)
        i = h
        t = self.table

        while t[i] != -1:
            if t[i] == x:
                return True
            
            i = (i+1) % self.cap

            if i == h:
                return False
        return False

    def remove(self,x):
        h = self.hash(x)
        i = h
        t = self.table
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True

            i = (i+1) % self.cap

            if i == h:
                return False
        return False        

h = MyHash(7)
print(h.table)
h.insert(58)
print(h.table)
h.insert(63)
print(h.table)
h.insert(78)
print(h.table)
h.insert(59)
print(h.table)
h.insert(62)
print(h.table)
h.insert(67)
h.insert(76)
print(h.table)
print(h.search(59))
print(h.remove(59))
print(h.search(59))