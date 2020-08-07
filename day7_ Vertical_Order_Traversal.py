# DFS
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        hmap = defaultdict(list)
        self.min = 0
        self.max = 0
        def dfs(root,x=0,y=0):
            if root:
                hmap[x].append((-y,root.val))
                self.min = min(self.min,x)
                self.max = max(self.max,x)
                dfs(root.left,x-1,y-1)
                dfs(root.right,x+1,y-1)
        dfs(root)
        self.ans = []    
        for x in range(self.min,self.max+1):
            self.ans.append([i[1] for i in sorted(hmap[x])])
        return self.ans

# BFS
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict,deque
        hmap = defaultdict(list)
        self.queue = deque()
        self.queue.append([root,0,0])
        self.min = 0
        self.max = 0
        def bfs():
            if self.queue:
                if self.queue[0][0]:
                    root,x,y = self.queue[0]
                    hmap[x].append((-y,root.val))
                    self.min = min(self.min,x)
                    self.max = max(self.max,x)
                    self.queue.append([root.left,x-1,y-1])
                    self.queue.append([root.right,x+1,y-1])
                self.queue.popleft()
                bfs()
        bfs()
        self.ans = []    
        for x in range(self.min,self.max+1):
            self.ans.append([i[1] for i in sorted(hmap[x])])
        return self.ans