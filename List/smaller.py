# Return list of elements smaller than x
def smaller(l,x):
    small = []
    for i in l:
        if i <= x:
            small.append(i)
    
    return small

# Time Complexity => O(n)

print(smaller([10,11,2,3,5,7,8],10))
