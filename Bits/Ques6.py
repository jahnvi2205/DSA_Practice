 def findPosition(self, n):
        # code here 
        # A number has exactly one set bit iff n & (n - 1) == 0
        if n==0 or (n & (n-1)!=0):
            return -1
          
        pos= 0  
        while n>0:
            n=n>>1
            pos+=1
            
        return pos
            
        