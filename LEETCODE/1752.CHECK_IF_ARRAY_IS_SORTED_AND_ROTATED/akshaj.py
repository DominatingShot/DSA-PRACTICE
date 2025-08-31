class Solution:
    def check(self, nums:list[int]) -> bool:
        x = nums[0]
        i=0
        while(i<(len(nums)-1) and nums[i]<=nums[i+1]):
            i+=1
        if(i==len(nums)-1):
            return True
        i+=1
        if(nums[i]>x):
            return False
        for i in range(i,len(nums)-1):
            if(nums[i]>nums[i+1] or nums[i+1]>x):
                return False
        return True