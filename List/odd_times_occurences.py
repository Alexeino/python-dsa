def odd_occurence_item(l):
    dic = dict()
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
    # To be continued
l = [10,10,20,30,30,30,30]

# print(odd_occurence_item(l))

def odd_item(l):
    res = 0
    for x in l:
        res = res ^ x
    return res

print(odd_item(l))