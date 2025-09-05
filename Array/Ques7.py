def rotate(self, arr):   #rotate once
        temp=arr[-1]
        i=len(arr)-1
        
        while i>0:
            arr[i]=arr[i-1]
            i-= 1
            
        arr[0]=temp




        # if rotation by k
        # temp=arr[:]
        # for old in range(len(arr)):
        #     new= (old+k)%len(arr)
        #     arr[new] = temp[old]

        # return arr