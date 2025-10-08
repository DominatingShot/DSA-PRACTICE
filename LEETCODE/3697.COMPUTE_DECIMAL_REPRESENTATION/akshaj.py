from typing import List
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        l = []
        y = 0
        while(n>0):
            x = n%10
            if(x>0):
                l.append(x*(10**y))
            y+=1
            n=n//10
        return l[::-1]