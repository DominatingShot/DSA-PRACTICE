class Solution:
    def doesAliceWin(self, s: str) -> bool:
        l = [0] * len(s)
        x = 0
        for i in range(0,len(s)):
            if(s[i] in "aeiou"):
                x+=1
            l[i] = x
        action = True
        evod = 1
        while(action):
            x = len(s)-1
            action = False
            while(x>=0 and l[x]!=-1):
            
                if(l[x]%2 == evod):
                    for i in range(x+1,len(s)):
                        l[i] = l[i]-l[x]
                    l[x] = -1
                    evod = evod^1
                    action = True
                    break
                x-=1
        if(evod == 0):
            return True
        return False

                    


            