def romanToDecimal(self, s): 
        Nums= {"I":1, "V":5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
        ans= 0
        
        for i in range(len(s)):
            if i>0 and Nums[s[i-1]]<Nums[s[i]]:
                ans-= Nums[s[i-1]]
                ans+= (Nums[s[i]]-Nums[s[i-1]]) 
            
            else:
                ans+= Nums[s[i]]
            
        return ans