from sys import maxsize as inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        b1, b2 = inf, inf
        p1, p2 = 0, 0
        for n in prices:
            b1 = min(b1, n)
            p1 = max(p1, n-b1)

            b2 = min(b2, n-p1)
            p2 = max(p2, n-b2)
        return p2
