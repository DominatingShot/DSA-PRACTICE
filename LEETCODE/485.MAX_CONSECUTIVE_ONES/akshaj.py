from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        temp = 0
        for i in nums:
            if i==1:
                temp += 1
            else:
                m=max(temp,m)
                temp = 0
        m=max(temp,m)
        return m
            