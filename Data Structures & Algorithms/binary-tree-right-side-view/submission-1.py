# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        right_side = [root.val]
        while(len(queue) > 0):
            # print(right_side)
            temp_queue = []
            while(len(queue) > 0):
                node = queue.pop(0)
                if node.left is not None:
                    temp_queue.append(node.left)
                if node.right is not None:
                    temp_queue.append(node.right)
            if len(temp_queue) > 0:
                right_side.append(temp_queue[-1].val)
            queue = temp_queue
        return right_side
                
        