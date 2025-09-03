def productExceptSelf(self, arr):
        prefix= 1
        res= [1]*len(arr)
        for i in range(len(arr)):
            res[i]=prefix
            prefix*=arr[i]
            
        suffix=1
        for i in range(len(arr)-1,-1,-1):
            res[i]*=suffix
            suffix*=arr[i]
            
        return res