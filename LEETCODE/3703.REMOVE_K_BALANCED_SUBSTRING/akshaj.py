class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        os = 0  
        cs = 0 
        ans = ""
        j = 0
        n = len(s)
        while j < n:
            ch = s[j]
            if ch == "(":
                if cs > 0:
                    ans += "(" * os + ")" * cs
                    os = 0
                    cs = 0
                os += 1
            else:
                cs += 1
          
                while os >= k and cs >= k:
                    os -= k
                    cs -= k 

            j += 1

   
        ans += "(" * os + ")" * cs
        if(ans != s):
            return self.removeSubstring(ans,k)
        return ans
