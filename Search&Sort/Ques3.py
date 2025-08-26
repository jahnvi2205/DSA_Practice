def find_pivot(self,nums):
        start=0
        end=len(nums)-1
        while start<=end:
            if start==end:
                return start
            mid= (start+end)//2
            if mid+1<len(nums) and nums[mid]> nums[mid+1]:
                return mid
            elif mid-1>=0 and nums[mid]< nums[mid-1]:
                return mid-1
            elif nums[start]> nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return -1


    def binary_search(self,nums,start,end,target):
        while start<=end:
            mid= (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1



    def search(self, nums: List[int], target: int) -> int:        
        pivot=self.find_pivot(nums)
        if target>=nums[0] and target<=nums[pivot]:
            return self.binary_search(nums,0,pivot,target)
        return self.binary_search(nums,pivot+1,len(nums)-1,target)
        