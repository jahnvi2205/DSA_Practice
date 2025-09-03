def findMaxSum(self,arr):
        # code here
        prev2= arr[0]
        prev1= max(arr[1],arr[0])
        for i in range(2,len(arr)):
            op1=arr[i]+prev2
            op2= prev1
            curr= max(op1,op2)
            prev2=prev1
            prev1=curr
            
        return prev1