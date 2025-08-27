def sortedMatrix(self,N,Mat):
        arr=[]
        for i in range(N):
            for j in range(N):
                arr.append(Mat[i][j])
                
        arr.sort()
        k=0
        for i in range(N):
            for j in range(N):
                Mat[i][j]=arr[k]
                k+=1
                
        return Mat