# Input: s = "geeksforgeeks"
# Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]

def counter(s):
    
    s= "".join(sorted(s))
    i=0
    while i<len(s):
        count=1
        while i+1 <len(s) and s[i]==s[i+1]:
            count+= 1
            i+=1
        
        if count>1:
            print([s[i],count],end=", ")

        i+= 1

