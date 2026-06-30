# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while(True):
            if node is None:
                break
            node = node.next
            size += 1
        print(size)
        count = 0
        node = head
        while(True):
            if node is None:
                break
            if node.next is None:
                head = head.next
                break
            if count == size - n - 1:
                node.next = node.next.next
                break
            node = node.next
            count += 1
        return head
        