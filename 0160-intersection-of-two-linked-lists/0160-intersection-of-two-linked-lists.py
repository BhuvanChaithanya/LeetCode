# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        while head2 != None:
            temp = head1
            while temp != None:
                if temp == head2:
                    return head2

                temp = temp.next

            head2 = head2.next

        return None