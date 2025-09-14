def maxhistogram(self,heights):
        heights= heights+ [0]
        max_area= 0
        n= len(heights)
        s= []

        i= 0
        while i< n:
            if (not s) or (heights[i]> heights[s[-1]]):
                s.append(i)
                i+=1

            else:
                top= s.pop()
                height= heights[top]
                width= i if (not s) else (i-s[-1]-1)
                # print(height*width)
                max_area= max(max_area, height*width)

        return max_area
        
        
        
    def maxArea(self, mat):
        row=len(mat)
        col=len(mat[0])
        h=[0]* col
        max_area= -float('inf')
         
        for i in range(row):
            for j in range(col):
                h[j]= h[j]+1 if mat[i][j]==1 else 0
            
            max_area= max(max_area, self.maxhistogram(h))  
            
        return max_area
            