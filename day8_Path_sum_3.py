# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def findSum(root):
            if root:
                traverse(root, sum)
                findSum(root.left)
                findSum(root.right)

        def traverse(root, target):
            if root:
                if root.val == target:
                    self.allPaths += 1
                traverse(root.left, target-root.val)
                traverse(root.right, target-root.val)

        self.allPaths = 0
        findSum(root)
        return self.allPaths


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.traverse(root, sum) +\
                self.pathSum(root.left, sum) +\
                self.pathSum(root.right, sum)
        else:
            return 0

    def traverse(self, root, target):
        if root:
            return int(root.val == target) + \
                self.traverse(root.left, target-root.val) +\
                self.traverse(root.right, target-root.val)
        else:
            return 0
