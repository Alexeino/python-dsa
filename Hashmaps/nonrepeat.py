from collections import Counter
ls = [0,9,2,3,4,8,7]

def printNonRepeated(arr):
    #Your code here
    counter = dict(Counter(arr))
    ls = []
    for k,v in counter.items():
        if v == 1:
            ls.append(k)
    return ls

r1 = printNonRepeated(ls)
print(r1)