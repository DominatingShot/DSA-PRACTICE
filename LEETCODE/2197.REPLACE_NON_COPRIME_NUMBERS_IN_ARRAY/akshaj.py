from typing import List
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):
            if(b==0):
                return a
            return gcd(b,a%b)
        if(len(nums) <= 1):
            return nums
        ans = [nums[0]]
        i = 1
        while i < len(nums):
            x = gcd(ans[-1],nums[i])
            if(x>1):
                y = (ans[-1]*nums[i])//x
                ans.pop()
                while(len(ans)>0):
                    z= gcd(y,ans[-1])
                    if(z>1):
                        y = (ans[-1]*y)//z
                        ans.pop()
                    else:
                        break
                ans.append(y)
            else:
                ans.append(nums[i])
            i+=1        
        return ans
        
        