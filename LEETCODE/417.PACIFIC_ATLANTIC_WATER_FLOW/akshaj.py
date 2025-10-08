from typing import List
class Solution:
    l = [[1,0],[0,1],[-1,0],[0,-1]]
    def dfs(self,i,j,vis,heights):
        vis[i][j] = True
        for k in self.l:
            x = i + k[0]
            y = j + k[1]
            if(x>=0 and y>=0 and x<len(heights) and y<len(heights[0]) and vis[x][y]!= True and heights[i][j]<=heights[x][y]):
                self.dfs(x,y,vis,heights)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        n = len(heights)
        m =  len(heights[0])
        atl = [[False]*m for i in range(n)]
        pac =  [[False]*m for i in range(n)]

        for i in range(n):
            self.dfs(i,0,pac,heights)
            self.dfs(i,m-1,atl,heights)
        for j in range(m):
            self.dfs(0,j,pac,heights)
            self.dfs(n-1,j,atl,heights)
        ans = []
        for i in range(n):
            for j in range(m):
                if(atl[i][j] and  pac[i][j]):
                    ans.append([i,j])
        return ans


        
        

