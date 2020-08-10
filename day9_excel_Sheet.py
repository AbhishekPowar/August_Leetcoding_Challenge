class Solution:
    def titleToNumber(self, s):
        num = 0
        for letter in s:
            num = num*26 + (ord(letter)-64)
        return num


if __name__ == "__main__":
    sol = Solution()
    ans = sol.titleToNumber('ABHI')
    print(ans)
