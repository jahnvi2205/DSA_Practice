def sortBySetBitCount(self, arr, n):
    def countSetBits(num):
        count=0
        while num:
            count+= num&1
            num= num>>1
        return count
            
    # Step 1: Store (-bits, index, value)
    temp = []
        
    for i in range(n):
        bits= countSetBits(arr[i])
        temp.append((-bits,i,arr[i]))
            
    temp.sort()
        
    # put temp back in arr
    for i in range(n):
        arr[i]= temp[i][2] 