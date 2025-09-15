class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp = ""
        c = 0
        ans = ""
        for i in s:
            temp+=i
            if i  == "(":
                c += 1
            else:
                c -= 1
            if(c==0):
                ans += temp[1:-1:1]
                temp = ""
        return ans