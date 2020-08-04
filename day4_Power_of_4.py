class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return 0
        numB = f'{num:b}'
        return numB.count('1') == 1 and numB.count('0') % 2 == 0


# Better solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num-1)) == 0 and (num-1) % 3 == 0
