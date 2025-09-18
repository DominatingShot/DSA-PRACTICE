class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        for i in s:
            l[ord(i)-ord("a")] += 1
        for i in t:
            l[ord(i)-ord("a")] -= 1  
        for i in l:
            if i != 0:
                return False
        return True     
