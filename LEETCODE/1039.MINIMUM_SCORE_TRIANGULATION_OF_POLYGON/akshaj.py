from math import inf

class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = inf
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])

        return dp[0][n - 1]
