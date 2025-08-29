def subArrayExists(self,arr):
        prefix=0
        seen=set()
        for i in arr:
            prefix+=i
            if prefix==0 or prefix in seen:
                return True
            seen.add(prefix)
            
        return False