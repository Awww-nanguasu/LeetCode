# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#pointer ⭐⭐
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev_point = None
        head = list2

        while(1):
            if head is None:
                return list1

            if list1 is None:
                return head

            if list2 is None:
                prev_point.next = list1
                return head

            if list1.val >= list2.val:
                if list2.next is None or list1.val < list2.next.val:
                    prev_point = list1
                    next_point = list1.next
                    list1.next = list2.next
                    list2.next = list1
                    list1 = next_point
                    list2 = prev_point.next
                else:
                    list2 = list2.next

            else:
                if prev_point is None:
                    next_point = list1.next
                    head = list1
                    list1.next = list2
                    list1 = next_point
                    list2 = head
                else:
                    prev_point.next = list1
                    next_point = list1.next
                    list1.next = list2
                    prev_point = list1
                    list1 = next_point
            
        return list2

