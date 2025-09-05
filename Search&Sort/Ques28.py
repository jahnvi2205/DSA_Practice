def inSequence(self, a, b, c):
        # Opt:1  
        # i=1
        # while i<=b:
        #     An= a+(i-1)*c
        #     if An==b:
        #         return True
        #     elif An>b:
        #         return False
        #     i+=1
            
        # return False
        
        
        # Opt:2 
        # if c==0:
        #     if a==b:
        #         return True
        #     else:
        #         return False
                
        # N= (b-a)//c +1
        # if b== a+(N-1)*c and N>0:
        #     return True
        # return False
        
        
        # Opt:3
        if c==0 and a==b:
            return True
            
        N= (b-a)/c +1
        
        if N==int(N) and N>=0:
            return True
        return False