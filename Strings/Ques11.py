def findPermutation(self, s):
        result=set()
        
        def backtrack(path,remain):
            if not remain:
                result.add(path)
                return
            
            for i in range(len(remain)):
                backtrack(path+remain[i], remain[:i]+remain[i+1:])
            
            
        backtrack("",s)
        return list(result)