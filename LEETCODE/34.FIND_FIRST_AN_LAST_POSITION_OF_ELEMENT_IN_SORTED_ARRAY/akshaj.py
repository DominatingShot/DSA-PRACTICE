from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while(l <= r):
            m = l + (r-l)//2
            if(nums[m] == target):
                x = m
                y = m
                while(x>0 and nums[x]==nums[x-1]):
                    x-=1
                while(y<(len(nums)-1) and nums[y]==nums[y+1]):
                    y+=1
                
                return [x,y]
            elif(nums[m]<target):
                l = m + 1
            else:
                r = m - 1
        return [-1,-1]
                
                 