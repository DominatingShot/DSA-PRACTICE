from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        while(i<n and nums[i]!=0):
            i+=1
        for j in range(i+1,n):
            if(nums[j]!=0):
                nums[i] = nums[j]
                nums[j] = 0
                while(i<n and nums[i]!=0):
                    i+=1