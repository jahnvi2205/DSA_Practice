def rev(arr):
    start, end= 0, len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end], arr[start]
        start+=1
        end-=1

    return arr


    

# Input= [1,3,5,7,9]
# Output= [9,7,5,3,1]

