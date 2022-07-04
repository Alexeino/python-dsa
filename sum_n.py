def sum_of_n(n):
    total = 0   #C
    for i in range(n+1): #Cn
        # print(i)
        total = total + i #C
    return total #C
# Ct = Cn + C + C + C => Cn + 3C => Cn + C
print(sum_of_n(5))