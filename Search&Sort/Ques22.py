def pivot(arr):
    start=0
    end=len(s)-1

    while s<e:
        mid= s+(e-s)//2

        if arr[mid]>arr[end]:
            start= mid+1
        else:
            end= mid

    return  arr[start]