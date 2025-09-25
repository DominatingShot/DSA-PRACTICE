class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n = len(v1)
        m = len(v2)
        if(n<=m):
            v1 += [0]*(m-n)
        else:
            v2 += [0]*(n-m)
        for k in range(len(v1)):
            i = v1[k]
            j = v2[k]
            if(int(i) == int(j)):
                continue
            else:
                return -1 if int(i)<int(j) else 1
        return 0