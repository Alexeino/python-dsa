l = [10,20,30,40]

def average(l):
    sum = 0 #k O(1)
    for i in l: #n
        sum += i #k O(n)
    
    n = len(l) #k O(1)
    return sum/n #k O(1)

# Time Complexity = k+k+k+kn => O(n)

print(average(l))
    