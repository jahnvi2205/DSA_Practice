def smallestSubWithSum(self, x, arr):
        n=len(arr)
        min_len=n+1
        curr_sum=0
        start=end=0
        while end<n:
            curr_sum += arr[end]
            while curr_sum>x:
                curr_sum-=arr[start]
                min_len=min(min_len,end-start+1)
                start+=1
            end+=1
            
        if min_len==n+1:
            return 0
        return min_len