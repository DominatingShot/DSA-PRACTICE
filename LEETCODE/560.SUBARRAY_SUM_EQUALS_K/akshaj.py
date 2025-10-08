from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        d = {}
        for i in range(len(nums)):
            s += nums[i]
            if(s in d.keys()):
                d[s] += 1
            else:
                d[s] = 1
        s = 0
        total = 0
        for i in range(len(nums)):
            if((k+s) in d.keys()):
                total += d[k+s]

            s+=nums[i]
            d[s]-=1
        return total
