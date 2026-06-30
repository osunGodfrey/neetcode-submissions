# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head
        while(True):
            stack.append(node)
            if node.next is None:
                break
            node = node.next
        # print(stack)
        reordered = head
        while(True):
            if reordered.next is None:
                break
            next_next = reordered.next
            # print("val", reordered.val)
            added_node = stack.pop()
            # print("add", added_node.val)
            next_added = stack.pop()
            next_added.next = None
            stack.append(next_added)
            added_node.next = next_next
            reordered.next = added_node
            reordered = next_next
            if reordered == added_node:
                break
        reordered.next = None
        # print(next_next.val)
        # head = reordered

    def printList(self, head: Optional[ListNode]) -> None:
        node = head
        while(True):
            print(node.val)
            if node.next is None:
                break
            node = node.next

        
        
        