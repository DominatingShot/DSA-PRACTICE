#https://www.youtube.com/watch?v=3vbHTi6sID0
class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)
    
# formula: F(n) = (phi^n - psi^n) / sqrt(5)
# where phi = (1 + sqrt(5)) / 2 and psi = (1 - sqrt(5)) / 2
