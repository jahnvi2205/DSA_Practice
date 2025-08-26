def valueEqualToIndex(self, arr):
        result=[]
        for i in range(len(arr)):
            if i+1==arr[i]:
                result.append(arr[i])
                
        return result