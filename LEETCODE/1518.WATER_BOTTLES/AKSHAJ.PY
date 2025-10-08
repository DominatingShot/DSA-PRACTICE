class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        e = 0
        while(numBottles>0):
            if(numBottles+e < numExchange):
                return total
            else:
                new_e = (numBottles + e)%numExchange
                numBottles = (numBottles + e)//numExchange
                total += numBottles
                e = new_e
        return total