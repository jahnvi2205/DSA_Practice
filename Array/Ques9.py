def getMinDiff(self, arr, k):
        if len(arr)==1:
            return 0
            
        n=len(arr)
        arr.sort()
        
        result= arr[-1]-arr[0]
        
        smallest= arr[0]+k
        largest= arr[-1]-k
        
        for i in range(0,n-1):
            min_height= min(smallest, arr[i+1]-k)
            max_height= max(largest, arr[i]+k)
            
            if min_height<0:
                continue
            
            result= min(result, max_height-min_height)
            
        return result