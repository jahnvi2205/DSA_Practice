def nextPermutation(self, arr):
        i=len(arr)-2
         # step 1: find first decreasing element
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        
        # step 2: find element just larger than arr[i] to swap
        if i>=0:    
            j=len(arr)-1
            while arr[j]<=arr[i]:
                j-=1
                    
            arr[i], arr[j]= arr[j], arr[i]
        
        # step 3: reverse the suffix
        left= i+1
        right= len(arr)-1
        while left<= right:
            arr[left],arr[right]= arr[right],arr[left]
            left+=1
            right-=1