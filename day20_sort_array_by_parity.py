class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        for r in range(len(A)):
            if A[l] % 2 == 0:
                l += 1
            elif A[r] % 2 == 0:
                A[l], A[r] = A[r], A[l]
                l += 1
        return A
# Explanation:
# R increments regardless
# L increments only when it is 0 or swap
# Pass 0:
# low = v
# A   = 0 0 1 1 0 1 0
# r   = ^
# ----------------
# Pass 2:
# low =   v
# A   = 0 0 1 1 0 1 0
# r   =   ^
# ----------------
# Pass 3:
# low =     v
# A   = 0 0 1 1 0 1 0
# r   =     ^
# ----------------
# Pass 4:
# low =     v
# A   = 0 0 1 1 0 1 0
# r   =       ^
# ----------------
# Pass 5:
# low =     v
# A   = 0 0 1 1 0 1 0
# r   =         ^
# # SWAP
# ----------------
# Pass 6:
# low =       v
# A   = 0 0 0 1 1 1 0
# r   =           ^
# ----------------
# Pass 7:
# low =       v
# A   = 0 0 0 1 1 1 0
# r   =             ^
# ----------------
# Pass 8:
# low =       v
# A   = 0 0 0 0 1 1 1
# r   =             ^
# # SWAP
# ----------------
