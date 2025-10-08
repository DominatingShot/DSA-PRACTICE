class Solution:
    
    def dfs(self,pos,carry,la,lb,n):
        if(pos == len(n)):
            return 1 if carry == 0 else 0

        target = int(n[pos])

        mina = 1 if(pos<la) else 0
        minb = 1 if(pos<lb) else 0
        maxa = 9 if(pos<la) else 0
        maxb =  9 if(pos<lb) else 0
        total = 0

        key = (pos, carry, la, lb) 
        if key in self.dp:
            return self.dp[key]

        for i in range(mina,maxa+1):
            for j in range(minb,maxb+1):
                temp = i + j + carry
                if((temp%10) == target):
                    total += self.dfs(pos+1,temp//10,la,lb,n)
        self.dp[key] = total
        return total


    def countNoZeroPairs(self, n: int) -> int:
        self.dp = {}
        si = len(str(n))
        n = str(n)[::-1]
        total = 0
        for i in range(1,si+1):
            for j in range(1,si+1):
                total += self.dfs(0,0,i,j,n)
        return total
