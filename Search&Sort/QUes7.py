def findTwoElement(self, arr):
        # code here
        # n=len(arr)
        # freq=[0]*(n+1)
        # rep=-1
        # miss=-1
        # for i in arr:
        #     freq[i]+=1
        # for i in range(1,n+1):
        #     if freq[i]==0:
        #         miss=i
        #     elif freq[i]==2:
        #         rep=i
                
        # return [rep,miss]
        
        n= len(arr)
        ASum= (n* (n+1))//2
        ASum2= (n * (n+1) * (2*n + 1))//6
        
        ObSum= 0
        ObSum2= 0
        for i in arr:
            ObSum+= i
            ObSum2+= (i*i)
            
            
        val1= ASum-ObSum
        
        val2= ASum2-ObSum2
        val2= val2//val1
        
        miss= (val1+val2)//2
        rep= val2-miss
        
        return [rep,miss]   

