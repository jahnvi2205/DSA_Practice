def is_pali(self, s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]

def longestPalindrome(self, s):
    result = ""
    for i in range(len(s)):
        # odd length palindrome
        pali1 = self.is_pali(s, i, i)
        if len(pali1) > len(result):
            result = pali1

        # even length palindrome
        pali2 = self.is_pali(s, i, i+1)
        if len(pali2) > len(result):
            result = pali2

    return result
