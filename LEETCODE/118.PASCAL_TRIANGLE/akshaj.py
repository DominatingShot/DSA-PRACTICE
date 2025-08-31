class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if(numRows==1):
            return [[1]]
        l = []
        l.append([1])
        for i in range(1,numRows):
            temp = []
            temp.append(1)
            x=l[i-1]
            for i in range(1,len(x)):
                temp.append(x[i-1]+x[i])
            temp.append(1)
            l.append(temp)
        return l
