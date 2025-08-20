# Input: s1 = "abcd", s2 = "cdab"
# Output: True

# def is_rotate(s1,s2):
#     return s1 in s2+s2

def is_rotate(s1,s2):
    n= len(s1)
    for _ in range(n):
        if s1==s2:
            return True
        s2= s2[-1]+ s2[:-1]

    return False

