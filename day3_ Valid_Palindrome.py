# Faster tah 99% of python solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^A-Za-z0-9]', '', s)
        s = s.lower()
        return s == s[::-1]


# O(n) space
# O(n) Time
# No function raw solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArr = []
        for letter in s:
            val = ord(letter)
            if ord('0') <= val <= ord('9') or ord('a') <= val <= ord('z'):
                sArr.append(letter)
            elif ord('A') <= val <= ord('Z'):
                sArr.append(chr(val+32))
        print(sArr)
        return sArr == sArr[::-1]
