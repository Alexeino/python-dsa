ls = [2, 2, 1, 7, 5, 3]
k = 4

combs =  [[a,b] for idx, a in enumerate(ls) for b in ls[idx+1:]]
print("Original List : ",combs)
new_l = []
for i in combs:
    print(i)
    if sum(i) % 4 == 0:
        new_l.append(i)
    else:
        pass

print("New List : ",new_l)