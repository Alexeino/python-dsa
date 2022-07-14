# Count the number of subarray present in an array that sums upto zero...
input = [15,-2,2,-8,1,7,10,23,-13,-8,-2]
# Output => [-2,2],[-8,1,7], => 2 

# Method 1 -> Maintaining a prefix_sum set/array and counter = 0, 
            # counter will be incremented whenever the element is zero or the pre_sum is already present in the prefix_sum set
            
def countSubarray(ls):
    pre_sum = 0
    counter = 0
    h = set()
    
    for i in range(len(ls)):
        pre_sum += ls[i]
        if pre_sum in h or ls[i] == 0:
            counter += 1
        h.add(pre_sum)
        
    return counter

c1 = countSubarray(input)
print(c1)