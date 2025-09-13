def findMinDiff(self, arr, M):
        arr.sort()
        ans= float('inf')
        
        for i in range(len(arr)-M+1):
            ans= min(ans, arr[i+M-1]-arr[i])
            
        return ans