from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        z = 1
        z1 = 1
        target = (x+y)//2
        if((x+y)%2 == 0):
            z = 2
            z1 = 2
            target -= 1

        i=0
        j=0
        ans = 0
        temp = 0
        while(i<x and j<y):
            if(nums1[i]<=nums2[j]):
                temp = nums1[i]
                if(i+j >= target):
                   
                    ans+=temp
                    z-=1
                    if(z<=0):
                        break
                i+=1
            else:
                temp = nums2[j]
                if(i+j >= target):
                   
                    ans+=temp
                    z-=1
                    if(z<=0):
                        break
                j+=1    
        while(i<x and z>0):
            temp = nums1[i]
            if(i+j >= target):
              
                ans+=temp
                z-=1
            i+=1

        while(j<y and z>0):
            temp = nums2[j]
            if(i+j >= target):
              
                ans+=temp
                z-=1
            j+=1

        return ans/z1

            