l1 = [10,200,5,50]
# Output = 20

def largest(l):
    for x in l:                 #x = 10, y=10,200,5,50
        for y in l:             #x = 200
            if y > x:
                break
        else:
            return x
    return None

# Time Complexity O(n^2)
# print(largest([l1]))

def largest_linear(l):
    if not l:
        return None
    else:
        result = l[0]
        # print(result)
        for i in range(1,len(l)):
            if l[i] > result:
                result = l[i]

        return result

# Time Complexity O(n)

print(largest_linear(l1))
