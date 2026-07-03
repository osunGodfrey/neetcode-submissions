# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addTwo(l1, l2):
            # next_node = addTwo(l1, l2)
            # print(l1, l2)
            if l1 is None and l2 is None:
                return None
            elif l1 is not None and l2 is None:
                if l1.val < 10:
                    return ListNode(l1.val, l1.next)
                else:
                    rem = (l1.val) % 10
                    carry = (l1.val) // 10
                    if l1.next is None:
                        return ListNode(rem, ListNode(carry, None))
                    l1.next.val += carry
                    # print(rem, carry)
                    return ListNode(rem, addTwo(l1.next, None))
            elif l1 is None and l2 is not None:
                rem = (l2.val) % 10
                carry = (l2.val) // 10
                if l2.next is None:
                    if carry == 0: return ListNode(rem, None)
                    return ListNode(rem, ListNode(carry, None))
                l2.next.val += carry
                # print(rem, carry)
                return ListNode(rem, addTwo(l2.next, None))
            elif (l1.val + l2.val) < 10:
                return ListNode(l1.val + l2.val, addTwo(l1.next,l2.next))
            else:
                # print(l1.val, l2.val)
                rem = (l1.val + l2.val) % 10
                carry = (l1.val + l2.val) // 10
                if l1.next is not None and l2.next is None:
                    l1.next.val += carry
                    return ListNode(rem, addTwo(l1.next, None))
                if l1.next is None and l2.next is not None:
                    l2.next.val += carry
                    return ListNode(rem, addTwo(None, l2.next))
                # print(rem, carry, l1.next.val)
                if l1.next is None and l2.next is None:
                    return ListNode(rem, ListNode(carry, None))
                l1.next.val += carry
                return ListNode(rem, addTwo(l1.next,l2.next))
        return addTwo(l1, l2)
        