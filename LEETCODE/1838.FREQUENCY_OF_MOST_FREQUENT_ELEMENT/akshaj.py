class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=[0]
        for x in nums:
            l.append(x+l[-1])
        i=0
        j=0
        m=1
        while j < len(nums):
            s = l[j+1] - l[i]
            total = nums[j]*(j-i+1) - s
            if(total > k):
                i+=1
            else:
                m = max(m,(j-i+1))
            j+=1
        return m
        
            
            
            