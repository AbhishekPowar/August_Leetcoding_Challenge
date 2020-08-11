class Solution:
    def hIndex(self, citations: List[int]) :
        if not citations:
            return 0
        citations.sort()
        N = len(citations)
        
        count=-1
        ans = -1
        validNum=0
        for idx in range(N-1,-1,-1):
            num = citations[idx]
            count = N-idx
            if num>0:
                validNum +=1
            if num and count >= num:
                ans=num
                break
        if ans==-1:
            return validNum
        return max(ans,count-1)
        