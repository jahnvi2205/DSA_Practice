def longestConsecutive(self,arr):
        arr=sorted(set(arr))
        i=1
        count=1
        ms=1
        while i<len(arr):
            if arr[i]==arr[i-1]+1:
                count+= 1
                ms= max(ms, count)
            else:
                count=1
            i+=1
                
        return ms
            