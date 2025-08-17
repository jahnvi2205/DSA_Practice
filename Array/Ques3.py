# Input: arr=[1,3,2,11,56,23,5,6]
#        k=2
# Output: (3, 11)

def mini_maxi(arr,k):
    for i in range(k-1):
        arr.remove(min(arr))
        arr.remove(max(arr))
    
    return min(arr),max(arr)

