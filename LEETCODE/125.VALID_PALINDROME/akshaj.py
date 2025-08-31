class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        s=s.lower()
        for i in s:
            if(i.isalnum()):
                x+=i
        return x == x[::-1]