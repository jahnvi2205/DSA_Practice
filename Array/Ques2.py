# Input: arr[] = {3, 5, 4, 1, 9}
# Output: (1, 9)

def min_max(arr):
    mini =arr[0]
    maxi = arr[0]
    for i in arr:
        if i>maxi:
            maxi=i
        elif i<mini:
            mini=i

    return mini,maxi

