# Program to find if list has a sublist which sums upto 0
input = [-3,4,-2,-1,1]
# Output = True, Explanation - [13,-3,-10] sums upto 0

#Method 1: Finding prefix sum and if a sum is repeated or is equal to zero then it does have a subarray

def hasSubarray(ls):
    pre_sum = 0
    h = set()
    for i in range(len(ls)):
        pre_sum += ls[i] # Increment pre_sum to i th element
        if pre_sum == 0: # If pre_sum == 0 or
            return True
        if pre_sum in h: # Sum already present in h
            return True
        h.add(pre_sum)   # If pre_sum not present in h then add pre_sum to h.
    return False

h1 = hasSubarray(input)
print(h1)
        
