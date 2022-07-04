s1 = {2,4,6,8}
s2 = {4,8}
s3 = {3,9}

# Disjoint => Returs True if two sets don't have common values
print(s1.isdisjoint(s2)) # False, s1 and s2 have common elements
print(s1.isdisjoint(s3)) # True, s1 and s3 don't have commong elements

# Subsets => Returns true if s1 is subset of s2, means s2 has all the values of s1
print("Subset ",s1 <= s2) # False, s1 is larger, hence s2 can't have all elements of s1

#Superset => Returns true if s1 is superset of s2, means s1 has all items of s2 in it.
print("Superset ",s1 >= s2) # False, s1 is larger, hence s2 can't have all elements of s1

# Proper Subset => s1 < s2, True if s2 has all values of s1 and it has more number of elements
print("Proper Subset ",s1 < s2) # False, Since s1 is larger

#Proper Superset => s1 > s2, True if s1 is proper superset (all elements of s2 and larger in size)
print("Proper Superset ",s1 > s2) # True, s1 is larger and has all the elements of s2 in it.