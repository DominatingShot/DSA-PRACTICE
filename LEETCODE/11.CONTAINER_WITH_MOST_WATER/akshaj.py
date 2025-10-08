from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans=(min(height[i],height[j])*(j-i))
        while(i<j):
            if(height[i]<height[j]):
                i+=1
                ans=max((min(height[i],height[j])*(j-i)),ans)
            else:
                j-=1
                ans=max((min(height[i],height[j])*(j-i)),ans)
        return ans

