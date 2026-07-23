# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        level_order = [[root.val]]
        while(len(queue) > 0):
            # print("str:", level_order)
            temp_queue = []
            while(len(queue) > 0):
                node = queue.pop(0)
                if node.left is not None:
                    temp_queue.append(node.left)
                if node.right is not None:
                    temp_queue.append(node.right)
            temp_queue_vals = []
            for n in temp_queue:
                temp_queue_vals.append(n.val)
            if len(temp_queue_vals) > 0:
                level_order.append(temp_queue_vals)
            queue = temp_queue
        return level_order
        