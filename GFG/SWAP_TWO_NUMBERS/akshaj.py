class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:        
        a = a+b
        b = b-a
        a = a+b
        b = -b
        return (a,b)