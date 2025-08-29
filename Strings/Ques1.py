# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverseString(s: List[str]):
        start= 0
        end= len(s)-1
        while start<= end:
            s[start],s[end]= s[end],s[start]
            start+= 1
            end-= 1

9,4