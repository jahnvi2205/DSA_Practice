def nextSmallerEle(arr):
    n = len(arr)
    resukt= [-1]*n
    stack=[]
    for i in range(n-1,-1,-1):

        while st and st[-1]>= arr[i]:
            st.pop()

        if st:
            result[i]=st[-1]
            
        stack.append(arr[i])

    return result
