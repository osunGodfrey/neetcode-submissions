# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isSubBalanced(root):
            if root is None:
                return True, 0
            isleft, leftHeight = isSubBalanced(root.left)
            isright, rightHeight = isSubBalanced(root.right)
            if abs(leftHeight - rightHeight) > 1:
                return False, max(leftHeight, rightHeight)
            if not (isleft and isright):
                return False, max(leftHeight, rightHeight)
            return True, 1 + max(leftHeight, rightHeight)
        isbalanced, maxheight = isSubBalanced(root)
        # print("is", isbalanced, "h", maxheight)
        return isbalanced
            
        