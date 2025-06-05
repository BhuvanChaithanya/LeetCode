# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        temp = dummy

        carry = 0

        while l1 is not None or l2 is not None or carry:
            tot = 0

            if l1 is not None:
                tot += l1.val
                l1 = l1.next

            if l2 is not None:
                tot += l2.val
                l2 = l2.next

            tot += carry

            carry = tot//10

            temp.next = ListNode(tot%10)

            temp = temp.next

        return dummy.next
