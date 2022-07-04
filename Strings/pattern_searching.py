txt = "geeks for geeks"
pat = "geeks"
# O/P = 0, 10

n = len(pat)
output = []
for i in range(len(txt)):
    if txt[i:(i+n)] == pat:
        output.append(i)
print(output)