# Program to print first non repeating character

from collections import Counter
    
def nonrepeatingCharacter(s):
    #code here
    map = dict()
    
    for char in s:
        if char in map.keys():
            map[char] += 1
        else:
            map[char] = 1
    
    for k,v in map.items():
        if v == 1:
            return k
    
    return "$"
s1 = nonrepeatingCharacter("hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs")
print(s1)