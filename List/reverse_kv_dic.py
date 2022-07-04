# Reversing the key and value of a dictionary

d1 = {101:"gfg",102:"practice",103:"ide"}
# Desired Output, new d2 = {"gfg":101,"practice":102,"ide":103}

d2 = {v:k for k,v in d1.items()}
print(d1)
print(d2)