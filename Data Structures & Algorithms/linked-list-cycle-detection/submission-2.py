# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        search = set()
        node = head
        while(True):
            if node is not None:
                if node not in search:
                    search.add(node)
                else:
                    return True
                node = node.next
            else:
                return False
        