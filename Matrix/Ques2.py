def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row= len(matrix)
        s=0
        e= row-1
        req_row=-1
        while(s<=e):
            m=s+(e-s)//2
            if matrix[m][-1]==target:
                return True
            elif matrix[m][-1]>target:
                req_row=m
                e=m-1
            else:
                s=m+1
        
        if req_row == -1:
            return False

        s=0
        col=matrix[req_row]
        e= len(col)-1
        while(s<=e):
            m=s+(e-s)//2
            if col[m]==target:
                return True
            elif col[m]>target:
                e=m-1
            else:s=m+1
        
        return False
        
        
         