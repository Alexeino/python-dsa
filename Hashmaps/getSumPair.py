# Program to count the pair with given sum
# I/p = [1,5,4,2] O/p = 2 bcos (1+5) AND (4+2)

# input = [1,5,5,7,1]
input = [3,3,3,3]
sum = 6
# Output = 2, 1+5 , 7+(-1)

def getPairCounts(input,sum):
    
    map = dict()
    for i in input:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
            
    print("Frequency Map - ",map)
    # Frequency Map -  {1:2,5:1,7:1}
    # ls - [1,5,7,1] => pair1 = (1+5), pair2 = (5+1) 
    
    # finding out the complementry of i in m, 
    # if matches increment counter by frequency of that complement.

    count = 0
    for i in input:
        if (sum-i) in map.keys():
            count += map[sum-i]
            
        if i == (sum-1):
            count -= 1
            
    
    return int(count/2)

s1 = getPairCounts(input,sum)
print(s1)
