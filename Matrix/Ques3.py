def median(self,mat):
        n = len(mat)
        m = len(mat[0])
        
        def countsmaller(mid):
            count= 0
            for i in range(n):
                j= m-1
                while j>=0 and mat[i][j]>mid:
                    j-=1
                count+= (j+1)
                
            return count
        
        low= min(row[0] for row in mat)
        high= max(row[-1] for row in mat)
        desired= (n*m+1)//2
        
        while low<high:
            mid= low+(high-low)//2
            
            if countsmaller(mid)>= desired:
                high= mid
            else:
                low= mid+1
            
        return low
    
    
