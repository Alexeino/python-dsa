ls = [15,-2,2,-8,1,7,10,23]
print(ls)

def largestSubarray(ls):
    pre_sum = 0
    map = {}
    start = 0
    end = 0
    for i in range(len(ls)):
        pre_sum += ls[i]
        
        map[i] = pre_sum
        
        
    return map
f1 = largestSubarray(ls)
print(f1)