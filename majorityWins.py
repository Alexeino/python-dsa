l = [1,2,1,2,1,2]

def majorityWins(arr,x,y):
    # code here
    d = dict()
    for item in arr:
        if item in d:
            d[item] += 1
        else :
            d[item] = 1
    print(d)
    if d[x] and d[y]:
        if d[x] < d[y]:
            return y
        elif d[x] > d[y]:
            return y
        else:
            print("both equal")
            if x < y:
                return x
            else :
                return y

print(majorityWins(l,1,2))