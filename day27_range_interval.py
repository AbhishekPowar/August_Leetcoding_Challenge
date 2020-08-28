class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = []
        for idx, val in enumerate(intervals):
            arr.append((val, idx))
        arr.sort()
        ans = [-1]*len(arr)
        for idx in range(len(arr)):
            ii, jj = arr[idx][0]
            for idx2 in range(idx+1, len(arr)):
                num = arr[idx2][0][0]
                if num >= jj:
                    ans[arr[idx][1]] = arr[idx2][1]
                    break
        return ans
