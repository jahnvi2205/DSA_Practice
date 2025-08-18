# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

def sort_neg(arr):
    start= 0
    end= len(arr)-1
    while start<=end:
        if arr[start]<0:
            start+=1
        elif arr[end]>=0:
            end-= 1
        else:
            arr[start],arr[end]= arr[end],arr[start]


arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
sort_neg(arr)
print(arr)
