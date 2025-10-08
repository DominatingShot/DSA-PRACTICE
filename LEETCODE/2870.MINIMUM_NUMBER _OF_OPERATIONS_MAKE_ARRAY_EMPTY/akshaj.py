from collections import Counter
class Solution:
    def minOperations(self, nums):
        freq = Counter(nums)
        ans = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            if count % 3 == 1:
                ans += (count // 3) - 1 + 2
            elif count % 3 == 2:
                ans += (count // 3) + 1
            else:
                ans += count // 3
        return ans
