def commonElements(self, arr1, arr2, arr3):
        m=len(arr1)
        n= len(arr2)
        o= len(arr3)
        i,j,k= 0,0,0
        result=[]
        while i<m and j<n and k<o:
            if arr1[i]==arr2[j] and arr2[j]==arr3[k]:
                if not result or result[-1]!= arr1[i]:
                    result.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr3[k]:
                j+=1
            else:
                k+=1
                
        return result if result else [-1]