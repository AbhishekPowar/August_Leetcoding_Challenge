class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def nCr(n, r):
            r = min(r, n-r)
            res = 1
            for i in range(0, r):
                res *= (n-i)/(r-i)
            return round(res)
        n = rowIndex
        pascal = [1]*(n+1)
        half = (n+1)//2
        for r in range(half+1):
            pascal[r] = nCr(n, r)
        for idx in range(half+1, n+1):
            pascal[idx] = pascal[n-idx]
        return pascal


'''
Example for row = 4
answer is [1,4,6,4,1]
ans[0] = [1]
ans[1] = 1*(4/1) = 4
ans[2] = 1* (4/1) (3/2) = 6
ans[3] = 1 (4/1) (3/2) * (2/3) = 4
ans[4] = 1 (4/1) *(3/2) * (2/3) * (1/4) = 1
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        dp = [1]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]*(n-i+1)//(i)
        return dp


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        dp = [1]*(n+1)
        half = (n+1)//2

        for i in range(1, half+1):
            dp[i] = dp[i-1]*(n-i+1)//(i)

        for idx in range(half+1, n):
            dp[idx] = dp[n-idx]
        return dp
