from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x = x^i
        if(sum(nums)==0):
            return 0
        if(x != 0):
            return len(nums)
        return len(nums)-1