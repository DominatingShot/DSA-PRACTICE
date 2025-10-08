from typing import List
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = -math.inf
        for i in nums:
            s+=i
            m=max(s,m)
            if(s<0):
                s = 0
        return m