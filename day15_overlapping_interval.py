class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        if intervals:
            N = len(intervals)
            count = 0
            intervals.sort()
            pi, pj = intervals[0]
            for i in range(1, N):
                i, j = intervals[i]
                if i < pj:
                    count += 1
                    if j < pj:
                        pi, pj = i, j
                else:
                    pi, pj = i, j

        return count


# How does this work
-  Count overlaps while minimising them
-  how
# Case 1:
# ------------A
# ----B
#      -----C
#         ----D
# B,C,D overlap A so consider only shorter one
# increment ovrelap though

# Case 2:
# ----------A
#       ------------E
# Consider A as E is more likely to overlap

# Case 3:
# -------------A
#                    ------------F
# Consider F
