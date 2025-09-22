class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        for i in range(len(s)):
            if(s[i] in d.keys()):
                if(d[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in d2.keys()): return False
                d[s[i]] = t[i]
                d2[t[i]] = s[i]
                
        return True
