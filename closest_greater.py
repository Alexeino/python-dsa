l = [10,12,14,16,18,20,17]
x = 16
temp = 999
out = -1
for i in l:
    if i > x and i < temp:
        temp = i
        out = temp
print(out)