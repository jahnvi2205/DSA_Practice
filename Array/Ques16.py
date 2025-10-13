class Solution:
    def inversionCount(self, arr):
        # Code Here
        return self.mergesort(arr,0,len(arr)-1)
        
        
    def mergesort(self,arr,start,end):
        if start>=end:
            return 0
            
        count=0
        mid= start +(end- start)//2
        
        count+= self.mergesort(arr,start,mid)
        count+= self.mergesort(arr,mid+1,end)
        count+= self.merge(arr,start,mid,end)
        
        return count
        
    def merge(self,arr,start,mid,end):
        i= start
        j= mid+1
        temp=[]
        count=0
        
        while i<=mid and j<=end:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
                
            else:
                temp.append(arr[j])
                j+=1
                count+= (mid-i+1)
                
        while i<=mid:
            temp.append(arr[i])
            i+=1
            
        while j<=end:
            temp.append(arr[j])
            j+=1
            
        i= start
        j=0
        
        while j<len(temp):
            arr[i]=temp[j]
            j+=1
            i+=1
                
        return count
        
        