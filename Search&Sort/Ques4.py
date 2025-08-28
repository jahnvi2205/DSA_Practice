def countSquares(self, n):
        count=0
        i=1
        while i*i<n:
            count+=1
            i+=1
                
        return count