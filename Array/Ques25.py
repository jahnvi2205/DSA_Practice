def countOccurence(self,arr, k):
        freq= {}
        x=len(arr)//k
        for i in arr:
            freq[i]=freq.get(i,0)+ 1
        
        sorted_keys = sorted(freq.keys())

        count=0
        for key in sorted_keys:
            if freq[key]> x:
                count+=1
                
        return count