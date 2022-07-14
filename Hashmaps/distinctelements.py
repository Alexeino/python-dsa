# Count the number of distinct elements in an array
input = [10,20,10,30,30,20]
# ouptut = 3 , Explaination - 3 distinct elements are there 10,20,30

# My Way method  1
def countDistinct(ls):
    map = dict()
    for item in ls:
        if item in map.keys():
            map[item] += 1
        else:
            map[item] = 1 
    return len(map.keys())

m1 = countDistinct(input)
print(m1)

# Method 2 using Set most efficient
def setcountDistinct(ls):
     # Interal hashing
    return len(set(ls))

m2 = setcountDistinct(input)
print(m2)