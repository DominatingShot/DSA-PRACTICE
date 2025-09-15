class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())[::-1]
        s = " ".join(map(lambda x:x[::-1],s.split()))
        return s