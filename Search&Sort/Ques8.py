from collections import Counter
class Solution:
    def majorityElement(self, arr):
        if len(arr)==1:
            return arr[0]
        freq= Counter(arr)
        for num,count in freq.items():
            if count>len(arr)//2:
                return num
                
        return -1