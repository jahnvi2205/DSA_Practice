def kthSmallest(self, mat, k):
        n=len(mat)
        def countsmall(mid):
            count=0
            j= n-1
            for i in range(n):
                while j>=0 and mat[i][j]>mid:
                    j-=1
                count+=(j+1)
            return count
            
            
        low= mat[0][0]
        high= mat[n-1][n-1]
            
        while low<high:
            mid= low+ (high-low)//2
            if countsmall(mid)>=k:
                high=mid
            else:
                low=mid+1
                    
        return low
        