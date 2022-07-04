l = [1,2,3,4,5]
s = 12
sums = []
for j in range(1,len(l)):
    ls = []
    for k in range(0,j+1):
        ls.append(l[k])
        print(l[k],end="")
    sums.append(sum(ls))

print(sums)