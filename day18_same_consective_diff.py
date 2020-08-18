class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = list(range(0, 10))
        if N > 1:
            ans = list(range(1, 10))

        for level in range(2, N+1):
            ans2 = []
            for num in ans:
                low = num % 10 - K
                high = num % 10 + K
                if high <= 9:
                    ans2.append(num*10+high)
                if low >= 0 and low != high:
                    ans2.append(num*10+low)
            ans = ans2[:]
        return ans
