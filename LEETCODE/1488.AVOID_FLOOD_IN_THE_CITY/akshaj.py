from typing import List
import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        lakes = {"leftover": []}
        n = len(rains)

        for i in range(n):
            if rains[i] != 0:
                lakes[rains[i]] = lakes.get(rains[i], i)

                if lakes[rains[i]] != i:
                    j = lakes[rains[i]]

                    k = bisect.bisect_right(lakes["leftover"], j)
                    if k == len(lakes["leftover"]):
                        return []
                    else:
                        ans[lakes["leftover"][k]] = rains[i]
                        lakes["leftover"].pop(k)

                    lakes[rains[i]] = i

                ans.append(-1)
            else:
                ans.append(0)
                lakes["leftover"].append(len(ans) - 1)

        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 1

        return ans
