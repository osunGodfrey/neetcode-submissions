"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = {}
        def recList(head):
            if head is None:
                # print(stack)
                stack[head] = None
                return None
            node = Node(head.val)
            stack[head] = node
            nextN = recList(head.next)
            # print(head.random)
            node.next, node.random = nextN, stack[head.random]
            return node
        return recList(head)
        