def spirallyTraverse(self, mat):
        left= 0
        right= len(mat[0])-1
        top= 0
        bottom= len(mat)-1
        output=[]
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                output.append(mat[top][i])
            top+= 1
            
            for i in range(top,bottom+1):
                output.append(mat[i][right])
            right-= 1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    output.append(mat[bottom][i])
                bottom-= 1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    output.append(mat[i][left])
                left+= 1
            
        return output


3,6,7,9