def celebrity(self, mat):
        n=len(mat)
        a=0
        b=n-1
        while a<b:
            if mat[a][b]==1:
                a+=1
            else:
                b-=1
                
        res=a
        for i in range(n):
            if i!=res:
                if mat[res][i]==1 or mat[i][res]==0:
                    return -1
                    
        return res