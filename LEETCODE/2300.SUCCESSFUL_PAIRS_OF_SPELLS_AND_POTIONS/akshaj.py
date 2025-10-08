from typing import List
import bisect
import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        min_array = list(map(lambda x: math.ceil(success/x),potions))
        min_array.reverse()
        for i in range(len(spells)):
            spells[i]=bisect.bisect_right(min_array, spells[i])   

        return spells