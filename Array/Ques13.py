def maxSubarraySum(self, arr):
        # Code here
        dp =[0]*len(arr)
        dp[0]=arr[0]
        for i in range(1,len(arr)):
            dp[i]= max(arr[i],dp[i-1]+arr[i])
            
        return max(dp)