# Input: arr = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]

def sort_012(arr):
    start= 0
    mid=0
    end= len(arr)-1
    while mid<=end:
        if arr[mid]== 0:
            arr[start],arr[mid]= arr[mid], arr[start]
            mid+= 1
            start+= 1

        elif arr[mid]== 1:
            mid+= 1
        else:
            arr[end],arr[mid]= arr[mid], arr[end]
            end-= 1
