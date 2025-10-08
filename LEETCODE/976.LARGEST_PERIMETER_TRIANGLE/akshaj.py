from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        ans = 0
        n = len(nums)
        for i in range(n-2):
            if(nums[i+1] + nums[i+2] > nums[i]):
                return nums[i+1] + nums[i+2] + nums[i]
        return 0
 