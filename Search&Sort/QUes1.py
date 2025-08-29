def find_occur(self,arr,target, search_first):
        start=0
        end=len(arr)-1
        result=-1
        while start<=end:
            mid= (start+end) //2
            if arr[mid]==x:
                result=mid
                if search_first:
                    end=mid-1
                else:
                    start=mid+1
                
            elif arr[mid]>x:
                end=mid-1
            else:
                start=mid+1
        
        return result
        
    def find(self, arr, x):
        first= self.find_occur(arr,x,True)
        last= self.find_occur(arr,x,False)
        return [first,last]
        

6