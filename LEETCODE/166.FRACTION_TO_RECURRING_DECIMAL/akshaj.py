class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        sign = ""
        if(n*d < 0):
            sign = "-"
        n,d = abs(n),abs(d)
        m = {}
        temp = ""
        rem = n
        front = 0
        if(n>=d):
            front = n//d
            rem = n%d
        front = str(front)
        rem = rem * 10
        x = 1
        back = ""
        i=0
        while(rem != 0):
            temp = str(rem//d)
            back += temp
            m[rem] = i
            i+=1
            rem = (rem%d) *10
            if(rem in m.keys()):
                ans = sign+front + "."+back[:m[rem]] +"("+back[m[rem]:]+")"
                return ans
        
        if(back!=""):
            return sign+front + "." +back
        return sign+front

            
                