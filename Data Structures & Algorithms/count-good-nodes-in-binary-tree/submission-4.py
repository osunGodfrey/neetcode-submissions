# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(root, maxval):
            if root is None:
                return 0
            lcounts = countGood(root.left, max(maxval, root.val))
            rcounts = countGood(root.right, max(maxval, root.val))
            counts = lcounts + rcounts
            if root.val >= maxval:
                counts += 1 
            # print(counts)
            return counts
        counts = countGood(root, root.val)
        return counts
        