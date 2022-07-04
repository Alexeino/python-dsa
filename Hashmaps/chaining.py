class MyHash():
    def __init__(self,length):
        self.length = length

        self.hash_table = [[] for i in range(length)]
        print(self.hash_table)

    def insert(self,key):
        i = key % self.length
        self.hash_table[i].append(key)
    
    def display(self):
        print(self.hash_table)
        
    def search(self,key):
        i = key % self.length
        print(key in self.hash_table[i])

    def remove(self,key):
        i = key % self.length
        if key in self.hash_table[i]:
            self.hash_table[i].remove(key)
        else:
            print("Key not found")

h1 = MyHash(7)
h1.insert(22)
h1.insert(43)
h1.insert(21)
h1.insert(24)
h1.insert(59)
h1.display()

h1.search(22)
h1.remove(22)
h1.search(22)