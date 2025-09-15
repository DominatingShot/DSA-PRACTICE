from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        newl= strs
        i = 0
        while(i<len(newl[0])):
            if(newl[0][i]!=newl[-1][i]):
                break
            i+=1
        return newl[0][:i:]