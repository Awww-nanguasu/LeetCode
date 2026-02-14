# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        cur_pointer = head
        next_pointer = head.next
        pre_pointer = None

        while next_pointer:
            if cur_pointer.val != next_pointer.val:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next
                next_pointer = next_pointer.next
            else:
                while(cur_pointer.val != next_pointer.val):
                    next_pointer = next_pointer.next
                    if next_pointer == None:
                        if pre_pointer == None:
                            return None
                        pre_pointer.next = None
                        return head

                cur_pointer = next_pointer
                next_pointer = next_pointer.next                
                pre_pointer.next = cur_pointer