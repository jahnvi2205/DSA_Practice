def areIsomorphic(self, s1, s2):
        # code here 
        if len(s1)!= len(s2):
            return False
            
        iso1, iso2= dict(), dict()
        
        for i,j in zip(s1,s2):
            if i in iso1 and iso1[i]!= j:
                return False
            if j in iso2 and iso2[j]!=i:
                return False
                
            iso1[i]= j
            iso2[j]= i
            
        
        return True  