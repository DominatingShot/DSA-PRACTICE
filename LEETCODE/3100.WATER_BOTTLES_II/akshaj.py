class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        e = numBottles
        while(e>0):
            if(e < numExchange):
                return numBottles
            else:
                e-=numExchange
                e+=1
                numBottles+=1
                numExchange+=1
        return numBottles