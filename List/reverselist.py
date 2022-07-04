def reverselist(l):
    start = 0
    end = len(l)-1

    while start < end:
        l[start],l[end] = l[end],l[start]
        start += 1
        end -=1
    
    return l

l1 = [10,20,30]
print(reverselist(l1))