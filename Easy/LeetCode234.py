# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.font_head = head

        def recur_check(curr):
            if curr == None:
                return True

            if curr.val != self.font_head.val:
                return False
            else:
                self.font_head = self.font_head.next
                return recur_check(curr.next)
        
        return recur_check(head)