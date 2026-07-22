# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxdepthdiam(root: Optional[TreeNode]):
            if root is None:
                return 0, 0
            leftdepth, leftdiam = maxdepthdiam(root.left)
            rightdepth, rightdiam = maxdepthdiam(root.right)
            return (1 + max(leftdepth, rightdepth)), max(leftdepth + rightdepth, max(leftdiam, rightdiam))
            # return 1 + max(maxdepth(root.left), maxdepth(root.right)), 
        depth, diam = maxdepthdiam(root)
        # print("depth:", depth, "diam:", diam)
        return max(depth - 1, diam)
        # return (1 if root.left is None or root.right is None else 0)
        