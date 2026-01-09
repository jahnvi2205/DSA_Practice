def isPalinArray(arr):
    for i in arr:
        if str(i)!= str(i)[::-1]:
            return False
            
    return True