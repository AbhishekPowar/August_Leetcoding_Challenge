class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if days:
            dp = [0]*(days[-1]+1)

            for d in days:
                dp[d] = 1

            def gets(dp, idx):
                if idx < 0:
                    return dp[0]
                else:
                    return dp[idx]

            for i in range(1, days[-1]+1):
                if dp[i] == 1:
                    c1 = gets(dp, i-1)+costs[0]
                    c7 = gets(dp, i-7)+costs[1]
                    c30 = gets(dp, i-30)+costs[2]
                    dp[i] = min(c1, c7, c30)
                else:
                    dp[i] = dp[i-1]
            return dp[-1]

# Explanation
# run algo twice
