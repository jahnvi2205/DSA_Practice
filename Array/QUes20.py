def rearrange(self,arr):
        pos=[x for x in arr if x>=0]
        neg= [x for x in arr if x<0]
        
        i=j=k=0
        while i<len(pos) and j<len(neg) and k<len(arr):
            if k%2==0:
                arr[k]=pos[i]
                i+=1
            else:
                arr[k]= neg[j]
                j+= 1
            k+=1
            
            
        while i<len(pos):
            arr[k]=pos[i]
            i+=1
            k+=1
            
        while j<len(neg):
            arr[k]=neg[j]
            j+=1
            k+=1