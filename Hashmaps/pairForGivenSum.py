# Program to find if the array has atleast 1 pair sums  upto given sum k
ls = [8,6,7,3]
k = 10
# Output - True, 6 & 4
def isPairSum(ls,k):
    for i in ls:
        print(k-i)
        if (k-i) in ls and (k-i) is not i:
            print("k-i",(k-i))
            print("i - ",i)
            return True
        
    return False
        

s1 = isPairSum(ls,k)
print(s1)