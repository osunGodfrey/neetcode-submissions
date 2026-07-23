# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def removeMin(maxval, array):
            for index, val in enumerate(array):
                if val < maxval:
                    array[index] = -1000
            return array

        def findGood(root):
            if root is None:
                return []
            lGoodList = findGood(root.left)
            rGoodList = findGood(root.right)
            lGoodList = removeMin(root.val, lGoodList)
            rGoodList = removeMin(root.val, rGoodList)
            # print([root.val] + lGoodList + rGoodList)
            return [root.val] + lGoodList + rGoodList

        finarray = findGood(root)
        count = 0
        for val in finarray:
            if val > -1000:
                count += 1
        return count

            
        