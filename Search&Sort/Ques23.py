def kthElement(self, a, b, k):
        i=0
        j=0
        count=0
        ans= min(a[0],b[0])
        
        while i<len(a) and j<len(b):
            if a[i] <= b[j]:
                ans=a[i]
                i+=1
                count+=1
            else:
                ans=b[j]
                j+=1
                count+=1
                
            if count==k:
                return ans
                
        if count!=k:
            while i<len(a):
                ans=a[i]
                i+=1
                count+=1
                if count==k:
                    return ans
                
            while j<len(b):
                ans=b[j]
                j+=1
                count+=1
                if count==k:
                    return ans
            
        return ans
            