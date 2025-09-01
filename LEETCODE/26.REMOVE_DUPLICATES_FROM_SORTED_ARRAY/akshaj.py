class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        s = set()
        for j in range(len(nums)):
            if nums[j] not in s:
                s.add(nums[j])
                nums[i]=nums[j]
                i+=1
        return i