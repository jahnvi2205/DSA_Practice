def union(arr1,arr2):
    i=0
    j=0
    ans=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]== arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1

    while i<len(arr1):
        ans.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        ans.append(arr2[j])
        j+=1

    return ans




def intersection(arr1,arr2):
    # arr1,arr2 are sorted
    i=0
    j=0
    ans=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]== arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1

    return ans

print(union([1,2,3,4],[2,4,5,6]))

