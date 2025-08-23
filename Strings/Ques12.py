def maxSubStr(self,str):
        ans= 0
        balance=0
        
        for i in str:
            balance+=1 if i=="1" else -1
            if balance==0:
                ans+=1
            
        if balance!=0:
            return -1
        return ans