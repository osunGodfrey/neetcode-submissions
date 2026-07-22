# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        queue = [root]
        while(len(queue) > 0):
            # [print(n.val, end = ", ")  for n in queue if n is not None ]
            # print()
            depth += 1
            temp_queue = []
            while(len(queue) > 0):
                node = queue.pop()
                if node.left is not None:
                    temp_queue.append(node.left)
                if node.right is not None:
                    temp_queue.append(node.right)
            queue = temp_queue
        return depth
            



        
            
                
        
        