# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        last_node = None
        next_node = None
        while(True):
            if head.next is None:
                next_node = head.next
                head.next = last_node
                last_node = head
                head = next_node
                break
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
        return last_node

        