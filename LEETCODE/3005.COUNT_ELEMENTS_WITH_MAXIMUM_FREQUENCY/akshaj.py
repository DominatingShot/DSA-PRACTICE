from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        m = 0
        total = 0
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
            m = max(m,d[i])
        for i in d.values():
            if(i==m):
                total += 1
        return total*m
        