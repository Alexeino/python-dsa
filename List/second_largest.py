l = [5,10,15,40,20]
def second_largest(l):
    if  len(l) <= 1:
        return None 

    largest = l[0]
    sec_largest = None

    for x in l[1:]:
        if x > largest:
            sec_largest = largest
            largest = x
        elif x!= largest:
            if sec_largest == None or sec_largest < x:
                sec_largest = x
    
    return sec_largest
print(second_largest(l))

# Time Complexity O(n)
