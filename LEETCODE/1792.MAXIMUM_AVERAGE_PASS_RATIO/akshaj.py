#heapify, heappush, heappop, heappushpop, heapreplace, nlargest, nsmallest
import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        l = []
        for i in range(len(classes)):
            p,q = classes[i]
            l.append([-(((p + 1) / (q + 1)) - (p / q)), i])  

        heapq.heapify(l)
        
        while extraStudents > 0:
            temp = heapq.heappop(l)
            classes[temp[1]][0] += 1
            classes[temp[1]][1] += 1
            p,q = classes[temp[1]]
            heapq.heappush(l,[-(((p + 1) / (q + 1)) - (p / q)), temp[1]])
            extraStudents -= 1

        s=0
        for p,q in classes:
            s += (p/q)

        return s/len(l)
