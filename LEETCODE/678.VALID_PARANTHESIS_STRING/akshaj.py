class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = [0] * len(s)
        star = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=="*"):
                star+=1
            dp[i] = star
        l = []
        star = 0
        for i in range(0,len(s)):
            if(s[i] == "*"):
                star+=1
            elif(s[i] == "("):
                l.append(i)
            else:
                if(len(l)>0):
                    l.pop()
                elif(star>0):
                    star -= 1
                else: 
                    return False
        dif = 0
        
        if(len(l)>0):
            while(len(l)>0):
                x = l[-1]
                if(dp[x]-dif > 0):
                    l.pop()
                    dif += 1
                else:
                  
                    return False
        return True
            

