# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def isValidLeft(root, minint, maxint):
            if root is None:
                return True
            if not ((minint <= root.val) and (root.val < maxint)):
                return False
            # print("root:", root.val, "interval:", (minint, maxint))
            lvalid = isValidLeft(root.left, minint, root.val)
            rvalid = isValidRight(root.right, root.val, maxint)
            return (lvalid and rvalid)


        def isValidRight(root, minint, maxint):
            if root is None:
                return True
            if not ((minint < root.val) and (root.val < maxint)):
                return False
            # print("root:", root.val, "interval:", (minint, maxint))
            lvalid = isValidLeft(root.left, minint, root.val)
            rvalid = isValidRight(root.right, root.val, maxint)
            return (lvalid and rvalid)
        # isValidLeft(root, -100, root.val)
        # isValidRight(root, root.val, 100)
        return  isValidLeft(root.left, float('-inf'), root.val) and isValidRight(root.right, root.val, float('inf'))
        


        