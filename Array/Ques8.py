def maxSubarraySum(self, arr):
        dp =[0]*len(arr)
        dp[0]=arr[0]
        for i in range(1,len(arr)):
            dp[i]= max(arr[i],dp[i-1]+arr[i])
            
        return max(dp)


# dp[i]= max sum of subarray ending at index i including arr[i]