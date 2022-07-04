def is_sorted(l):

    if len(l) == 0 or len(l) ==1:
        return True
    for i in range(len(l)-1):
        print(l[i],l[i+1])
        if l[i] > l[i+1]:
            return False
    return True


l1 = [10,20,35,25,30,40]
print(is_sorted([]))
print(is_sorted([99]))
print(is_sorted(l1))

# Time Complexity O(n)