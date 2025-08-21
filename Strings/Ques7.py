def helper1(self,s:str) -> str:
        result=""
        i=0
        while i<len(s):
            count=1
            while i+1<len(s) and s[i]==s[i+1]:
                count+=1
                i+=1
            result += str(count)+str(s[i])
            i+=1

        return result


    def countAndSay(self, n: int) -> str:
        
        result="1"
        for _ in range(n-1):
            result = self.helper1(result)

        return result