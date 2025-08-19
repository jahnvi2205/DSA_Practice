def rotate(self, arr):
        temp=arr[-1]
        i=len(arr)-1
        
        while i>0:
            arr[i]=arr[i-1]
            i-= 1
            
        arr[0]=temp