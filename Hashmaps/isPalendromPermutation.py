# Writing a program to find if a string has permutation which is palendrome
# E.g. :- "aabbcc" => one permutation of this would be abccba, bcos it can be read same from both left and right
# Requirements:- For a number to be palindrome, character's frequency should be even and only 1 char is allowed to have odd
                # frequency bcos we can put 1 extra char in the middle of the permuted string
                # E.g. abacc => acbca can be read same from both left and right
from collections import Counter
def isPalindrome(string):
    counter = Counter(string)
    odd = 0
    for i in counter.values():
        if i % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True
    
i1 = "abacce"    # False
m1 = isPalindrome(i1)  
print(m1)

i2 = "abacc"    # True
m2 = isPalindrome(i2)
print(m2)