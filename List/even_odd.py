#Seperate even and odd

def seperate(l):
    even=[]     #k
    odd=[]      #k
    for i in l: #n
        if i%2==0: #k
            even.append(i) #k
        else: #k
            odd.append(i) #k
    
    print(even) #k
    print(odd) #k
# Time complexity : O(n)

seperate([10,11,12,13])