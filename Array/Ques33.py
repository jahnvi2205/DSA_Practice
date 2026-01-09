def minSwap (self,arr, k) : 
        good= 0
        for i in arr:
            if i<=k:
                good+=1
                
        if good ==0:
            return 0
            
        bad=0
        for i in range(good):
            if arr[i]>k:
                bad+=1
                
        ans= bad
        i=0
        j=good
        while j<len(arr):
            if arr[i]>k:
                bad-=1
                
            if arr[j]>k:
                bad+=1
                
            ans= min(ans, bad)
            i+=1
            j+=1
        
        return ans
    

