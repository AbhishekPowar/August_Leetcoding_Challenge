class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) >= 2:
            first = ord('A') <= ord(word[0]) <= ord('Z')
            second = ord('A') <= ord(word[1]) <= ord('Z')

            first = word[0].isupper()
            second = word[1].isupper()
            if first and second:
                low = 'A'
                high = 'Z'
            else:
                low = 'a'
                high = 'z'

            for i in word[1:]:
                if not ord(low) <= ord(i) <= ord(high):
                    return False

        return True

# pythonic solution


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) >= 2:
            if word[:2].isupper():
                return word[1:].isupper()
            else:
                return word[1:].islower()
        return True
