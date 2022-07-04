l = [10,22,12,16,18,15]
x = 16

temp = 0
out = 0
for i in l:
    if i < x and i > temp:
        temp = i 
        out = temp

print(out)
print(temp)