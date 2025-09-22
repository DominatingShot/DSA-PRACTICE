from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        total = 0
        ma = nums[0]
        mi = nums[0]
        for i in nums:
            ma = max(ma,i)
            mi = min(mi,i)
        return (ma - mi) * k