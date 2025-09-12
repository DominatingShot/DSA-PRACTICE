class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        s = 0
        while len(nums) > 1:
            temp = list(map(lambda x,y: (x+y)%10,nums,nums[1:]))
            nums = temp
        return nums[0]