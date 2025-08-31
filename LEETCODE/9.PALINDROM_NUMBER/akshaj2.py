class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        n = x
        rev = 0
        while(n>0):
            t = n%10
            rev = rev*10+t
            n = n//10
        return rev == x