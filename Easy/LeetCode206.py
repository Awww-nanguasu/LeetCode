# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, flag = 0):
        if head == None:
            dummy = ListNode()
            return dummy, dummy

        dummy, tmp = self.reverse(head.next)
        tmp.next = head
        return dummy, head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy, _ = self.reverse(head)
        head.next = None
        return dummy.next