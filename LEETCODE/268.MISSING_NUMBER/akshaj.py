from  typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = list(range(0,len(nums)+1))
        for i in nums:
            l[i] = -1
        for i in l:
            if(i!=-1):
                return i