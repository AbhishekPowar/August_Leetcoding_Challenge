from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        hmap = Counter(s)
        length = 0
        flag = 0
        for key in hmap:
            val = hmap[key]
            if val % 2 == 0:
                length += val
            else:
                flag = 1
                length += val-1
        return length+flag


# Betetr approach Single iteration


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hset = set()
        length = 0
        for ch in s:
            if ch in hset:
                hset.remove(ch)
                length += 2
            else:
                hset.add(ch)
        return length + int(len(hset) > 0)
