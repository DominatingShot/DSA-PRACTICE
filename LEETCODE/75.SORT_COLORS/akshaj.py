from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        j=len(nums)-1
        k = i
        while(k<=j):
            if(nums[k]==1):
                k+=1
            elif(nums[k]==2):
                nums[k] = nums[j]
                nums[j] = 2
                j-=1
            else:
                nums[k] = nums[i]
                nums[i] = 0
                i+=1
                k=i
            