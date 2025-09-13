def maxWater(self, arr):
        left= [0]*len(arr)
        right= [0]*len(arr)
        total_level= [0]*len(arr)
        
        # max left boundary
        left[0]= arr[0]
        for i in range(1, len(arr)):
            left[i]= max(left[i-1], arr[i])
         
        #max right boundary   
        right[-1]= arr[-1]
        for i in range(len(arr)-2,-1,-1):
            right[i]=max(right[i+1],arr[i])
            
        # total_level= water_level+ arr(height)
        for i in range(len(arr)):
            total_level[i]= min(left[i],right[i])
          
          
        water =0
        for i in range(len(arr)):
            water+= (total_level[i]- arr[i])
            
        return water