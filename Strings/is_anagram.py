s1 = "aabcd"
s2 = "bcdaa"
# O/p = True

s3 = "abdcc"
s4 = "aabdcc"
# o/p = False

def is_anagram(s1,s2):
    if len(s1) != len(s2):
        print(False)

    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for x in count:
        if x!=0:
            return False
    return True

print(is_anagram(s1,s2))