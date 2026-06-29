# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1
        node = list1
        val1 = node.val
        val2 = list2.val
        last_val2 = -1
        if val1 > val2:
            added_node = list2
            list2 = list2.next
            added_node.next = node
            node = added_node
            list1 = node
        while(True):
            if node is None: return list1
            if list2 is None: return list1
            val1 = node.val
            val2 = list2.val
            # next_val1 = node.next.val
            # print("point", node.val)
            # shift
            if node.next is not None:
                if node.next.val <= val2:
                    node = node.next
                    continue
            if val1 <= val2:
                added_node = list2
                list2 = list2.next
                added_node.next = node.next
                node.next = added_node
                node = added_node
                last_val2 = val2
                # print("add:", added_node.val)
            else:
                node = node.next





        