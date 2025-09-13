class Solution:
    def maxFreqSum(self, s: str) -> int:
        vc = 0
        cc = 0
        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for i in d.keys():
            if i in "aeiou":
                vc = max(d[i],vc)
            else:
                cc = max(d[i],cc)
        return vc + cc
