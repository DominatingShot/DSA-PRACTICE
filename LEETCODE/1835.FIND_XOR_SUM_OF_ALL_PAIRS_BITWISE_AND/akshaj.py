from typing import List
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x = 0
        for i in arr2:
            x = x ^ i
        y = 0
        for j in arr1:
            y = y^j
        return x & y