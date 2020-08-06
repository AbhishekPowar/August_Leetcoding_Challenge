# Hash Solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        self.ans = []
        seen = set()
        for i in nums:
            if i in seen:
                self.ans.append(i)
            else:
                seen.add(i)
        return self.ans

# No extra space


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
            else:
                ans.append(abs(i))
        return ans
