import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.cumulativeSum = []
        self.rects = []
        self.Csum =0
        for x1,y1,x2,y2 in rects:
            points = (x2+1-x1)* (y2+1-y1)
            self.cumulativeSum.append(self.Csum+points)
            self.rects.append((x1,y1,x2+1-x1))
            self.Csum+=points


    def pick(self) -> List[int]:
        rand = random.randint(1,self.Csum)
        prev = 0
        
        for idx,count in enumerate(self.cumulativeSum):
            if count>= rand:
                break
            prev = count
            
        xlow,ylow,xrange = self.rects[idx]
        
        rc = rand-prev-1  #making it zero based
        
        x = xlow+ rc%xrange  #offset calc
        y = ylow+ rc//xrange #offset calc
        return (x,y)

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()



# Explanation

# Cumulative sum is stored in a variable


# 8 -- 9 --10 --11
# |    |    |    |
# 4 -- 5 -- 6 -- 7
# |    |    |    |
# 0 -- 1 -- 2 -- 3


# say x,y = 0,0

# points 5 would be 
# x5 = x + 5%4 ----> len of x
# y5 = y + 5//4

# why 4 as 3+1-0 ==4
 
# Incase u didn't get what solution says just try it for multiple values
