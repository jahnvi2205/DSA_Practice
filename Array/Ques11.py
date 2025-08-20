# def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]:
#                 return nums[i]

#         return len(nums)


def findDuplicate(self, nums: List[int]) -> int:
    for num in nums:
        idx = abs(num)              
        if nums[idx] < 0:           
            return idx              
        nums[idx] = -nums[idx]      

    return len(nums)