def medianOf2(self, a, b):
        n= len(a)
        low= 0
        high= n
        
        while low<=high:
            cutA= (low+high)//2
            cutB= n- cutA
            
            leftA= a[cutA-1] if cutA>0 else float('-inf')
            rightA= a[cutA] if cutA<n else float('inf')
            
            leftB= b[cutB-1] if cutB>0 else float('-inf')
            rightB= b[cutB] if cutB<n else float('inf')
            
            if leftA<=rightB and leftB<=rightA:
                return (max(leftA,leftB)+min(rightA,rightB))/ 2
                
            elif leftA>rightB:
                high= cutA-1
                
            else:
                low= cutA+1