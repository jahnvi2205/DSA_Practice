def setBits(self, n):
		setBits=0
		while n:
		    setBits+=1
		    n= n & (n-1)
		    
		return setBits

        
        # setBits=0
        # while n:
        #     if n%2==1:
        #         setBits+=1
                
        #     n= n//2
            
        # return setBits