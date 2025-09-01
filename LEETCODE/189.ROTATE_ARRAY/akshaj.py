from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l = len(nums)
        x = nums[-k::1] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = x[i]