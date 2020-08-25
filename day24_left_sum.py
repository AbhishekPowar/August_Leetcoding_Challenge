# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def left(root, isleft=0):
            if root:
                if isleft and root.left == None and root.right == None:
                    self.summ += root.val
                else:
                    if root.left:
                        left(root.left, isleft=1)
                    if root.right:
                        left(root.right, isleft=0)
        self.summ = 0
        left(root)
        return self.summ
