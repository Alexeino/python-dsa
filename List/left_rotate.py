l = [10,20,30,40]

def left_rotate(l):
    item = l.pop(0) #O(n)
    l.append(item) #O(1)
    return l

print(left_rotate(l))