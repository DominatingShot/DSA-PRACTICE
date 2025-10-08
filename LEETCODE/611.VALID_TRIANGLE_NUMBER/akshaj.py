from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        ans = 0
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            while(j<k):
                if(nums[k] + nums[j] <= nums[i]):
                    k-=1
                else:   
                    ans += (k - j)
                    j+=1
        return ans
