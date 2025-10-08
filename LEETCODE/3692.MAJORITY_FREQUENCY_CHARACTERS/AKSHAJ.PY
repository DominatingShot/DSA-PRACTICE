class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = {}
        ans = ""
        for i in s:
            if(i in d.keys()):
                d[i]+=1
            else:
                d[i] = 1
        l = [0]*len(s)
        for i in d.values():
            l[i-1]+=1
        max = len(l)-1
        
        for i in range(len(l)-1,-1,-1):

            if(l[max] < l[i]):
                max = i
                
        
        for i in d.keys():
           
            if(d[i] == (max+1)):
                ans+=i
             
        return ans
                
            
        