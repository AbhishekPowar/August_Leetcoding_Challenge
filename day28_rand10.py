# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ans=0
        for idx in range(10):
            ans+=(rand7()+idx)%10
        return 1+ (ans%10) 
        